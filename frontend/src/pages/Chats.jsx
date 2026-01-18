import { useEffect, useState } from "react";
import { sendMessage, getConversationDetail, getConversationList, createConversation } from "../services/api";
import useAuthStore from '../state/useAuthStore';
import { useNavigate } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";

function Chats() {
  const [conversations, setConversations] = useState([]);
  const [activeConversation, setActiveConversation] = useState(null);
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const { access, refresh, doRefresh } = useAuthStore();
  const navigate = useNavigate();

  const loadConversations = async () => {
    try {
      const data = await getConversationList(access);
      setConversations(data || []);
    }
    catch(error) {
      if (error.response?.status == 401) {
        if (refresh == null) {
          navigate("/login")
        }
        try {
          doRefresh(refresh)
        }
        catch(error) {
          navigate("/login")
        }
      }
    }
  };
  
  const handleOpenConversation = async (conv) => {
    setActiveConversation(conv);
    setLoading(true);

    const data = await getConversationDetail(conv.id, access);
    setMessages(data["messages"] || []);

    setLoading(false);
  };

  const handleCreateConversation = async () => {
    const data = await createConversation("New conversation", access);

    setConversations((prev) => [data, ...prev]);
    setActiveConversation(data);
    setMessages([]);
  };

  const handleSendMessage = async () => {
    if (!newMessage.trim() || !activeConversation) return;

    const response = await sendMessage(
      newMessage,
      activeConversation.id,
      access
    );
    
    setMessages((prev) => [...prev, {text: newMessage, created_at: response.prompt_created_at}]);
    setMessages((prev) => [...prev, {text: response.reply, created_at: response.prompt_created_at}]);
    setNewMessage("");
  };

  useEffect(() => {
    if (access == null) {
      if (refresh == null) {
        navigate("/login")
      }
      try {
        doRefresh(refresh)
      }
      catch(error) {
        navigate("/login")
      }
    }
    loadConversations();
  }, []);

  return (
    <div style={styles.page}>
      <div style={styles.sidebar}>
        <button onClick={handleCreateConversation} style={styles.newButton}>
          + New conversation
        </button>

        {conversations.map((c) => (
          <button
            key={c.id}
            onClick={() => handleOpenConversation(c)}
            style={{
              ...styles.conversationButton,
              background:
                activeConversation?.id === c.id ? "#e0e0e0" : "transparent",
            }}
          >
            {c.title || "Untitled"}
          </button>
        ))}
      </div>

      <div style={styles.chat}>
        {!activeConversation ? (
          <p>Select or create a conversation</p>
        ) : (
          <>
            <div style={styles.messages}>
              {loading ? (
                <p>Loading...</p>
              ) : messages.length === 0 ? (
                <p>No messages yet</p>
              ) : (
                messages.map((m) => (
                  <div key={m.created_at} style={styles.message}>
                    {m.text}
                  </div>
                ))
              )}
            </div>

            <div style={styles.inputBar}>
              <input
                value={newMessage}
                onChange={(e) => setNewMessage(e.target.value)}
                placeholder="Type a message"
                style={styles.input}
              />
              <button onClick={handleSendMessage}>Send</button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

const styles = {
  page: {
    display: "flex",
    height: "100vh",
  },
  sidebar: {
    width: 280,
    borderRight: "1px solid #ccc",
    padding: 12,
    display: "flex",
    flexDirection: "column",
    gap: 8,
  },
  newButton: {
    marginBottom: 12,
  },
  conversationButton: {
    textAlign: "left",
    padding: 8,
    border: "none",
    cursor: "pointer",
  },
  chat: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    padding: 16,
  },
  messages: {
    flex: 1,
    overflowY: "auto",
    marginBottom: 12,
  },
  message: {
    padding: 8,
    marginBottom: 6,
    background: "#f5f5f5",
    borderRadius: 4,
  },
  inputBar: {
    display: "flex",
    gap: 8,
  },
  input: {
    flex: 1,
  },
};

export default Chats;
