---
title: 搜索
excerpt: Search for a page or post's content
---

{% include site-search.html %}

<!-- 
  =============================================================
  Modern Chatbot UI v2.0
  Author: Gemini Assistant & User
  Features: FAB, Fullscreen Modal, Mobile-first, Stop Generation,
            Markdown Typewriter Effect.
  =============================================================
-->

<!-- Chatbot FAB (Floating Action Button) -->
<div id="chat-fab-button" class="chat-fab-button">
  <!-- Chat Icon -->
  <svg class="chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.17L4 17.17V4h16v12zM11 6h2v6h-2V6zm0 8h2v2h-2v-2z"/>
  </svg>
</div>

<!-- Chat Overlay and Modal Window -->
<div id="chat-overlay" class="chat-overlay hidden">
  <div id="chat-modal" class="chat-modal">
    <div class="chat-header">
      <span class="chat-title">佛法问答</span>
      <button id="chat-close-button" class="chat-close-button" aria-label="关闭聊天">&times;</button>
    </div>
    <div id="chat-messages" class="chat-messages">
      <div class="message bot-message">
        <div class="message-content">阿弥陀佛，请问有什么可以帮助您？</div>
      </div>
    </div>
    <div class="chat-input-area">
      <textarea id="chat-input" placeholder="输入您的问题..." rows="1" aria-label="输入聊天信息"></textarea>
      <button id="chat-submit-button" class="chat-submit-button" aria-label="发送">
        <!-- Send Icon -->
        <svg id="send-icon" class="chat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24px" height="24px">
            <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
        </svg>
        <!-- Stop Icon (hidden by default) -->
        <svg id="stop-icon" class="chat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24px" height="24px" style="display: none;">
            <path d="M6 6h12v12H6z"/>
        </svg>
      </button>
    </div>
  </div>
</div>

<!-- Dependencies: Markdown Parser (marked.js) and HTML Sanitizer (DOMPurify) -->
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.11/dist/purify.min.js"></script>


<style>
/* Reset and Base Styles to avoid conflicts */
.chat-fab-button, .chat-modal, .chat-modal * {
    font-family: sans-serif; /* Use a consistent, clean font for the chat UI */
    box-sizing: border-box;
    line-height: 1.5; /* Reset line-height */
}

/* Chat FAB Button */
.chat-fab-button {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 56px;
    height: 56px;
    border: none;
    background-color: #3a77d8; /* Match page accent color */
    color: #fff;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    transition: all 0.2s ease-in-out;
    -webkit-tap-highlight-color: transparent;
}
.chat-fab-button:hover {
    background-color: #2e60ad;
    transform: translateY(-2px);
}
.chat-fab-button .chat-icon {
    width: 28px;
    height: 28px;
    fill: currentColor;
}

/* Chat Overlay (for modal background) */
.chat-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(44, 62, 80, 0.6); /* Use a color from the theme for the overlay */
    z-index: 1100;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 1;
    visibility: visible;
    transition: opacity 0.3s ease, visibility 0.3s ease;
}
.chat-overlay.hidden {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

/* Chat Modal */
.chat-modal {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
    display: flex;
    flex-direction: column;
    max-width: 650px;
    width: 90%;
    height: 80vh;
    max-height: 700px;
    overflow: hidden;
    transform: scale(1);
    transition: transform 0.3s ease;
}
.chat-overlay.hidden .chat-modal {
    transform: scale(0.95);
}

/* Header */
.chat-header {
    background: #f4f6f8;
    color: #2c3e50;
    padding: 12px 20px;
    border-bottom: 1px solid #e0e0e0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
    font-size: 1rem;
    flex-shrink: 0;
}
.chat-close-button {
    background: none;
    border: none;
    font-size: 1.8rem;
    line-height: 1;
    cursor: pointer;
    color: #a8adac;
    padding: 0 5px;
    transition: color 0.2s ease;
}
.chat-close-button:hover { color: #2c3e50; }

/* Messages Container */
.chat-messages {
    flex-grow: 1;
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
    font-size: 1rem;
}

/* Individual Message Styles */
.chat-messages .message {
    max-width: 85%;
    padding: 10px 15px; /* Reduced padding for better height */
    border-radius: 18px;
    word-wrap: break-word;
    box-shadow: 0 1px 2px rgba(0,0,0,0.08);
    line-height: 1.6; /* Improved readability */
}
.chat-messages .user-message {
    background: #dcf8c6;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}
.chat-messages .bot-message {
    background: #f4f6f8;
    align-self: flex-start;
    border-bottom-left-radius: 4px;
}

/* Markdown Rendering Styles (within message-content) */
.message-content { color: #2c3e50; }
.message-content > *:first-child { margin-top: 0; }
.message-content > *:last-child { margin-bottom: 0; }
.message-content p { margin: 0.5em 0; }
.message-content a { color: #3a77d8; text-decoration: underline; }
.message-content strong { font-weight: 700; }
.message-content ul, .message-content ol { padding-left: 20px; margin: 0.5em 0; }
.message-content code { background-color: #e0e0e0; padding: 2px 5px; border-radius: 4px; font-size: 0.9em; }
.message-content pre { background-color: #f4f6f8; padding: 10px; border-radius: 6px; overflow-x: auto; }
.message-content pre code { background: none; padding: 0; }
.message-content blockquote { border-left: 3px solid #a8adac; padding-left: 10px; margin: 0.5em 0; color: #555; }

/* Input Area */
.chat-input-area {
    display: flex;
    align-items: center;
    padding: 10px 15px;
    border-top: 1px solid #e0e0e0;
    background: #fff;
    flex-shrink: 0;
}
.chat-input-area textarea {
    flex-grow: 1;
    border: 1px solid #ccc;
    border-radius: 20px;
    padding: 8px 15px;
    resize: none;
    max-height: 120px;
    font-size: 1rem;
    line-height: 1.5;
    outline: none;
    transition: border-color 0.2s ease;
}
.chat-input-area textarea:focus { border-color: #3a77d8; }

.chat-submit-button {
    background: #3a77d8;
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    margin-left: 10px;
    cursor: pointer;
    flex-shrink: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.2s ease;
    color: white;
    -webkit-tap-highlight-color: transparent;
}
.chat-submit-button:hover:not(:disabled) {
    background-color: #2e60ad;
    transform: scale(1.05);
}
.chat-submit-button:disabled {
    background-color: #a8adac;
    cursor: not-allowed;
    transform: none;
}
.chat-submit-button .chat-icon { fill: currentColor; }

/* Mobile Responsive adjustments */
@media (max-width: 768px) {
    .chat-modal {
        width: 100%;
        height: 100%;
        max-height: 100vh;
        border-radius: 0;
    }
    .chat-header { padding: 12px 15px; }
    .chat-messages { padding: 15px; font-size: 0.95rem; }
    .chat-input-area { padding: 8px 10px; }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // --- Configuration ---
    const WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat';
    
    // --- State Management ---
    let fetchController = null; // To manage aborting the fetch request
    let typingInterval = null;  // To manage the typewriter effect interval

    // --- DOM Elements ---
    const chatFabButton = document.getElementById('chat-fab-button');
    const chatOverlay = document.getElementById('chat-overlay');
    const chatModal = document.getElementById('chat-modal');
    const chatCloseButton = document.getElementById('chat-close-button');
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const chatSubmitButton = document.getElementById('chat-submit-button');
    const sendIcon = document.getElementById('send-icon');
    const stopIcon = document.getElementById('stop-icon');

    // --- Markdown Parser Setup ---
    marked.setOptions({
        renderer: new marked.Renderer(),
        gfm: true,
        breaks: true,
    });
    const sanitize = DOMPurify.sanitize;

    // --- UI Logic ---
    const openChat = () => {
        chatOverlay.classList.remove('hidden');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
        setTimeout(() => chatInput.focus(), 300); // Focus after transition
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    const closeChat = () => {
        stopFetching(); // Stop any ongoing AI response
        chatOverlay.classList.add('hidden');
        document.body.style.overflow = ''; // Restore background scrolling
    };
    
    const setButtonState = (state) => {
        if (state === 'thinking') {
            chatInput.disabled = true;
            chatSubmitButton.disabled = false; // Keep button enabled for stopping
            chatSubmitButton.setAttribute('aria-label', '停止');
            sendIcon.style.display = 'none';
            stopIcon.style.display = 'block';
        } else { // 'idle' state
            chatInput.disabled = false;
            chatSubmitButton.disabled = false;
            chatSubmitButton.setAttribute('aria-label', '发送');
            sendIcon.style.display = 'block';
            stopIcon.style.display = 'none';
            chatInput.focus();
        }
    };

    // --- Core Functionality ---
    const typeMessage = (messageElement, fullMarkdown, delay = 20) => {
        return new Promise((resolve) => {
            if (typingInterval) clearInterval(typingInterval);
            
            messageElement.innerHTML = '';
            const fullHtml = sanitize(marked.parse(fullMarkdown));
            let i = 0;

            typingInterval = setInterval(() => {
                if (i < fullHtml.length) {
                    messageElement.innerHTML += fullHtml[i];
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                    i++;
                } else {
                    clearInterval(typingInterval);
                    typingInterval = null;
                    resolve();
                }
            }, delay);
        });
    };
    
    const stopFetching = () => {
        if (fetchController) {
            fetchController.abort();
            fetchController = null;
        }
        if (typingInterval) {
            clearInterval(typingInterval);
            typingInterval = null;
        }
        setButtonState('idle');
    };
    
    const sendMessage = async () => {
        const query = chatInput.value.trim();
        if (!query) return;

        stopFetching(); // Clear any previous state
        
        // --- Add User Message ---
        const userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'message user-message';
        const userMessageContent = document.createElement('div');
        userMessageContent.className = 'message-content';
        userMessageContent.textContent = query;
        userMessageDiv.appendChild(userMessageContent);
        chatMessages.appendChild(userMessageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        chatInput.value = '';
        chatInput.style.height = 'auto';
        setButtonState('thinking');

        // --- Add Bot Placeholder ---
        const botThinkingDiv = document.createElement('div');
        botThinkingDiv.className = 'message bot-message';
        const botThinkingContent = document.createElement('div');
        botThinkingContent.className = 'message-content';
        botThinkingContent.innerHTML = '<span class="thinking-cursor"></span>'; // Blinking cursor
        botThinkingDiv.appendChild(botThinkingContent);
        chatMessages.appendChild(botThinkingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        try {
            fetchController = new AbortController();
            const response = await fetch(WORKER_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query }),
                signal: fetchController.signal
            });

            if (!response.ok) {
                throw new Error(`API 请求失败: ${response.statusText}`);
            }

            const data = await response.json();
            await typeMessage(botThinkingContent, data.answer);

        } catch (error) {
            if (error.name === 'AbortError') {
                botThinkingContent.textContent = '已停止生成。';
            } else {
                console.error('Chat error:', error);
                botThinkingContent.innerHTML = sanitize(marked.parse('抱歉，服务出现了一点问题，请稍后再试。'));
            }
        } finally {
            if (fetchController && !fetchController.signal.aborted) {
                setButtonState('idle');
            }
            fetchController = null;
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    };

    // --- Event Listeners ---
    chatFabButton.addEventListener('click', openChat);
    chatCloseButton.addEventListener('click', closeChat);
    chatOverlay.addEventListener('click', (e) => { if (e.target === chatOverlay) closeChat(); });
    
    chatSubmitButton.addEventListener('click', () => {
        if (stopIcon.style.display === 'block') {
            stopFetching();
        } else {
            sendMessage();
        }
    });

    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Auto-resize textarea
    chatInput.addEventListener('input', () => {
        chatInput.style.height = 'auto';
        chatInput.style.height = `${chatInput.scrollHeight}px`;
    });
});
</script>