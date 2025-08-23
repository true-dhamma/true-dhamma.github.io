---
title: 搜索
excerpt: Search for a page or post's content
---

{% include site-search.html %}

<!-- Chatbot FAB Button -->
<div id="chat-fab-button" class="chat-fab-button">
  <svg class="chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="currentColor">
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
      <button id="chat-submit" class="chat-submit">发送</button>
    </div>
  </div>
</div>

<!-- Markdown Parser CDN -->
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.11/dist/purify.min.js"></script>


<style>
/* Chat FAB Button */
.chat-fab-button {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 56px; /* Slightly larger for better touch target */
    height: 56px;
    border: none;
    background-color: #3a77d8; /* Match accent color */
    color: #fff; /* Icon color */
    border-radius: 50%;
    cursor: pointer;
    padding: 0;
    box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    transition: all 0.2s ease-in-out;
    -webkit-tap-highlight-color: transparent; /* Remove tap highlight on mobile */
}
.chat-fab-button:hover {
    background-color: #2e60ad; /* Darker accent on hover */
    transform: translateY(-2px);
}
.chat-fab-button:active {
    transform: scale(0.95);
    box-shadow: 0 3px 8px rgba(0,0,0,0.2);
}
.chat-fab-button svg {
    width: 28px;
    height: 28px;
    fill: currentColor;
}

/* Chat Overlay (for modal background) */
.chat-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.6); /* Dim background */
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
    pointer-events: none; /* Allows clicks to pass through when hidden */
}

/* Chat Modal */
.chat-modal {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    display: flex;
    flex-direction: column;
    max-width: 600px; /* Desktop max width */
    width: 90%; /* Desktop initial width */
    height: 70vh; /* Desktop height */
    position: relative;
    overflow: hidden; /* Ensure content stays within bounds */
    transform: scale(1);
    transition: transform 0.3s ease;
}
.chat-overlay.hidden .chat-modal {
    transform: scale(0.95); /* Little animation on hide */
}

/* Header */
.chat-header {
    background: #f4f6f8; /* Light grey */
    color: #34495e; /* Dark text */
    padding: 15px 20px;
    border-bottom: 1px solid #e0e0e0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: bold;
    font-size: 1.1em;
}
.chat-close-button {
    background: none;
    border: none;
    font-size: 1.8em;
    cursor: pointer;
    color: #a8adac; /* Muted color for close icon */
    line-height: 1;
    padding: 0 5px;
    transition: color 0.2s ease;
}
.chat-close-button:hover {
    color: #2c3e50;
}

/* Messages Container */
.chat-messages {
    flex-grow: 1;
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
    line-height: 1.6; /* Improve readability */
    font-size: 0.95em; /* Slightly smaller font for messages */
}

/* Individual Message Styles */
.chat-messages .message {
    max-width: 85%;
    padding: 12px 16px;
    border-radius: 18px; /* More modern rounded corners */
    word-wrap: break-word; /* Ensure long words break */
    white-space: pre-wrap; /* Preserve whitespace and line breaks for markdown */
    box-shadow: 0 1px 2px rgba(0,0,0,0.08); /* Subtle shadow */
    font-family: sans-serif; /* Use sans-serif for chat messages */
}

.chat-messages .user-message {
    background: #dcf8c6; /* Light green */
    align-self: flex-end;
    border-bottom-right-radius: 4px; /* "Tail" effect */
}

.chat-messages .bot-message {
    background: #f4f6f8; /* Light grey */
    align-self: flex-start;
    border-bottom-left-radius: 4px; /* "Tail" effect */
}

/* Message content (Markdown rendering target) */
.message-content {
    /* Basic Markdown styling */
    color: #34495e;
}
.message-content strong,
.message-content b {
    font-weight: 700;
}
.message-content em,
.message-content i {
    font-style: italic;
}
.message-content a {
    color: #3a77d8;
    text-decoration: underline;
}
.message-content p {
    margin-bottom: 0.5em; /* Adjust paragraph spacing within markdown */
    margin-top: 0.5em;
}
.message-content p:first-child {
    margin-top: 0;
}
.message-content p:last-child {
    margin-bottom: 0;
}
.message-content ul,
.message-content ol {
    padding-left: 20px;
    margin: 0.5em 0;
}
.message-content li {
    margin-bottom: 0.2em;
}
.message-content blockquote {
    border-left: 4px solid #e0e0e0;
    padding-left: 10px;
    margin: 0.5em 0;
    color: #555;
}
.message-content pre {
    background-color: #eaeaea;
    border-radius: 4px;
    padding: 8px;
    font-family: monospace;
    overflow-x: auto;
}
.message-content code {
    background-color: #eaeaea;
    border-radius: 3px;
    padding: 2px 4px;
    font-family: monospace;
}
/* Ensure line breaks are respected for markdown-rendered content */
.message-content br {
    display: block; /* Treat <br> as block-level for consistent line height */
    margin-bottom: 0.5em; /* Add some space after line breaks */
}


/* Input Area */
.chat-input-area {
    display: flex;
    align-items: flex-end; /* Align input and button at bottom */
    padding: 15px 20px;
    border-top: 1px solid #e0e0e0;
    background: #fff; /* Keep input area white */
}

.chat-input-area textarea {
    flex-grow: 1;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 10px 15px;
    resize: none; /* Prevent manual resizing */
    max-height: 100px; /* Limit input height */
    font-size: 1rem;
    line-height: 1.5;
    outline: none;
    transition: border-color 0.2s ease;
    font-family: sans-serif; /* Use sans-serif for input */
}
.chat-input-area textarea:focus {
    border-color: #3a77d8;
}

.chat-input-area .chat-submit {
    background: #3a77d8;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    margin-left: 10px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: bold;
    transition: background-color 0.2s ease, transform 0.2s ease;
    min-width: 70px; /* Ensure button doesn't shrink too much */
    -webkit-tap-highlight-color: transparent;
}
.chat-input-area .chat-submit:hover:not(:disabled) {
    background-color: #2e60ad;
    transform: translateY(-1px);
}
.chat-input-area .chat-submit:disabled {
    background-color: #a8adac; /* Muted grey when disabled */
    cursor: not-allowed;
    transform: none;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .chat-fab-button {
        width: 50px;
        height: 50px;
        bottom: 20px;
        right: 20px;
    }
    .chat-fab-button svg {
        width: 24px;
        height: 24px;
    }
    .chat-modal {
        width: 95vw;
        height: 95vh;
        max-width: unset; /* Remove desktop max-width */
        border-radius: 8px;
    }
    .chat-header {
        padding: 12px 15px;
        font-size: 1em;
    }
    .chat-messages {
        padding: 15px;
        gap: 10px;
    }
    .chat-messages .message {
        padding: 10px 14px;
        border-radius: 16px;
    }
    .chat-input-area {
        padding: 12px 15px;
    }
    .chat-input-area textarea {
        padding: 8px 12px;
    }
    .chat-input-area .chat-submit {
        padding: 8px 15px;
        min-width: 60px;
    }
}
</style>

<script>
    // Initialize marked.js for parsing Markdown.
    // DOMPurify is used to sanitize the HTML output from Markdown parsing,
    // which helps prevent XSS vulnerabilities from untrusted Markdown content.
    marked.setOptions({
        renderer: new marked.Renderer(),
        gfm: true, // Use GitHub Flavored Markdown
        breaks: true, // Convert single line breaks to <br>
        sanitize: true, // Marked.js sanitize is deprecated in favor of DOMPurify
        // highlight: function(code, lang) { // Optional: for syntax highlighting in code blocks
        //     const hljs = window.hljs;
        //     if (hljs && lang && hljs.getLanguage(lang)) {
        //         return hljs.highlight(code, { language: lang }).value;
        //     }
        //     return code;
        // }
    });

    // Function to handle the typing effect with Markdown rendering
    async function typeMessage(messageElement, fullMarkdown, delay = 20) {
        if (window.typingInterval) { // Clear any previous typing effect
            clearInterval(window.typingInterval);
            window.typingInterval = null;
        }

        messageElement.innerHTML = ''; // Clear content first
        const fullHtml = DOMPurify.sanitize(marked.parse(fullMarkdown)); // Convert full markdown to sanitized HTML once
        let charIndex = 0;

        window.typingInterval = setInterval(() => {
            if (charIndex < fullHtml.length) {
                // Append one character at a time. The browser will render valid HTML tags as they complete.
                messageElement.innerHTML += fullHtml[charIndex];

                // Ensure scroll to bottom
                const chatMessages = document.getElementById('chat-messages');
                chatMessages.scrollTop = chatMessages.scrollHeight;
                charIndex++;
            } else {
                clearInterval(window.typingInterval);
                window.typingInterval = null;
            }
        }, delay);
    }

    document.addEventListener('DOMContentLoaded', () => {
        // DOM Elements
        const chatFabButton = document.getElementById('chat-fab-button');
        const chatOverlay = document.getElementById('chat-overlay');
        const chatModal = document.getElementById('chat-modal');
        const chatCloseButton = document.getElementById('chat-close-button');
        const chatMessages = document.getElementById('chat-messages');
        const chatInput = document.getElementById('chat-input');
        const chatSubmit = document.getElementById('chat-submit');

        // Replace with your KB-Chat Worker URL
        const WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat';

        // --- Chatbot UI Logic ---
        function openChat() {
            chatOverlay.classList.remove('hidden');
            chatInput.focus();
            chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom on open
        }

        function closeChat() {
            // Stop any ongoing typing effect
            if (window.typingInterval) {
                clearInterval(window.typingInterval);
                window.typingInterval = null;
            }
            chatOverlay.classList.add('hidden');
        }

        chatFabButton.addEventListener('click', openChat);
        chatCloseButton.addEventListener('click', closeChat);
        // Also close if clicking outside the modal (on the overlay itself)
        chatOverlay.addEventListener('click', (event) => {
            if (event.target === chatOverlay) {
                closeChat();
            }
        });

        // --- Message Handling Logic ---
        async function sendMessage() {
            const query = chatInput.value.trim();
            if (!query) return;

            // Clear any ongoing typing effect from previous bot message
            if (window.typingInterval) {
                clearInterval(window.typingInterval);
                window.typingInterval = null;
            }

            // Add user message
            const userMessageDiv = document.createElement('div');
            userMessageDiv.classList.add('message', 'user-message');
            const userMessageContent = document.createElement('div');
            userMessageContent.classList.add('message-content');
            userMessageContent.textContent = query;
            userMessageDiv.appendChild(userMessageContent);
            chatMessages.appendChild(userMessageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            chatInput.value = '';
            chatInput.style.height = 'auto'; // Reset textarea height
            chatSubmit.disabled = true;
            chatSubmit.textContent = '思考中...';

            // Add thinking message placeholder
            const botThinkingDiv = document.createElement('div');
            botThinkingDiv.classList.add('message', 'bot-message');
            const botThinkingContent = document.createElement('div');
            botThinkingContent.classList.add('message-content');
            botThinkingContent.textContent = '...'; // Initial placeholder
            botThinkingDiv.appendChild(botThinkingContent);
            chatMessages.appendChild(botThinkingDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            try {
                const response = await fetch(WORKER_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: query })
                });

                if (!response.ok) {
                    throw new Error(`API 请求失败: ${response.statusText}`);
                }

                const data = await response.json();
                const botAnswerMarkdown = data.answer;

                // Start typing effect for the bot's full answer
                await typeMessage(botThinkingContent, botAnswerMarkdown);

            } catch (error) {
                console.error('Chat error:', error);
                // If an error occurs, just set the error message without typing effect
                botThinkingContent.innerHTML = DOMPurify.sanitize(marked.parse('抱歉，服务出现了一点问题，请稍后再试。'));
            } finally {
                chatSubmit.disabled = false;
                chatSubmit.textContent = '发送';
                chatMessages.scrollTop = chatMessages.scrollHeight; // Ensure scroll to bottom after full message
            }
        }

        chatSubmit.addEventListener('click', sendMessage);
        chatInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' && !event.shiftKey) { // Allow shift+Enter for new line
                event.preventDefault(); // Prevent default new line
                sendMessage();
            }
        });

        // Auto-resize textarea
        chatInput.addEventListener('input', () => {
            chatInput.style.height = 'auto';
            chatInput.style.height = chatInput.scrollHeight + 'px';
        });
    });
</script>