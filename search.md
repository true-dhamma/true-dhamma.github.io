---
title: 搜索&问答
excerpt: Search for a page or post you're looking for
---

{% include site-search.html %}

<!-- Chatbot FAB and Window HTML -->
<div class="kb-chat-fab-container" id="kb-chat-fab-container">
  <button id="kb-chat-toggle-btn" class="kb-chat-fab-button" aria-label="打开/关闭佛法问答机器人">
    <!-- Chat Icon - Material Design style -->
    <svg class="kb-chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#FFFFFF">
      <path d="M0 0h24v24H0V0z" fill="none"/>
      <path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/>
    </svg>
  </button>
</div>

<div id="kb-chat-window" class="kb-chat-window">
  <div class="kb-chat-header">
    佛法问答
    <button id="kb-chat-close-btn" class="kb-chat-close-btn" aria-label="关闭聊天窗口">
      <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#FFFFFF">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
      </svg>
    </button>
  </div>
  <div id="kb-chat-messages" class="kb-chat-messages">
    <div class="kb-message kb-message--bot"></div> <!-- Initial message will be set by JS -->
  </div>
  <div class="kb-chat-input-container">
    <input type="text" id="kb-chat-input" placeholder="输入您的问题..." autocomplete="off" />
    <button id="kb-chat-send-btn" class="kb-chat-send-btn">
      <svg class="kb-chat-icon" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="currentColor">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2 .01 7z"/>
      </svg>
    </button>
  </div>
</div>

<!-- CSS Styles for Chatbot -->
<style>
  /* FAB Container */
  .kb-chat-fab-container {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 1000;
  }

  /* FAB Button */
  .kb-chat-fab-button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 56px;
    height: 56px;
    border: none;
    background-color: #007bff; /* Primary color */
    border-radius: 50%;
    cursor: pointer;
    padding: 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    transition: background-color 0.2s ease-in-out, transform 0.2s ease;
  }
  .kb-chat-fab-button:hover {
    background-color: #0056b3; /* Darker blue on hover */
    transform: translateY(-2px);
  }
  .kb-chat-fab-button:active {
    transform: scale(0.95);
  }
  .kb-chat-fab-button .kb-chat-icon {
    fill: white; /* Icon color */
    width: 28px; /* Slightly larger icon */
    height: 28px;
  }

  /* Chat Window */
  .kb-chat-window {
    position: fixed;
    bottom: 100px; /* Adjust based on FAB size/position */
    right: 20px;
    width: 380px; /* Wider window */
    height: 500px; /* Taller window */
    border-radius: 12px;
    background: #fff;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    display: flex;
    flex-direction: column;
    overflow: hidden; /* Ensures rounded corners */
    font-family: 'Roboto', 'Noto Sans CJK SC', sans-serif; /* Modern font, with Chinese fallback */
    color: #333;
    z-index: 999; /* Below FAB but above other content */
    transition: all 0.3s ease-in-out; /* Smooth open/close */
    transform: translateY(20px); /* Initial subtle offset for animation */
    opacity: 0; /* Initial hidden for animation */
    visibility: hidden; /* For screen readers */
  }
  .kb-chat-window.open {
    transform: translateY(0);
    opacity: 1;
    visibility: visible;
  }

  /* Header */
  .kb-chat-header {
    background: linear-gradient(to right, #007bff, #0056b3); /* Gradient header */
    color: white;
    padding: 15px 20px;
    font-size: 1.1em;
    font-weight: 500;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top-left-radius: 12px;
    border-top-right-radius: 12px;
  }
  .kb-chat-close-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 5px;
    margin-right: -5px; /* Adjust to align better visually */
  }
  .kb-chat-close-btn svg {
    fill: white; /* Close icon color */
    width: 20px;
    height: 20px;
  }
  .kb-chat-close-btn:hover svg {
    fill: #e0e0e0;
  }

  /* Messages Container */
  .kb-chat-messages {
    flex-grow: 1;
    overflow-y: auto;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: #f9f9f9; /* Light background for messages */
  }
  /* Scrollbar styles for modern look */
  .kb-chat-messages::-webkit-scrollbar { width: 8px; }
  .kb-chat-messages::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 10px; }
  .kb-chat-messages::-webkit-scrollbar-thumb { background: #888; border-radius: 10px; }
  .kb-chat-messages::-webkit-scrollbar-thumb:hover { background: #555; }

  /* Message Bubbles */
  .kb-message {
    padding: 10px 15px;
    border-radius: 18px; /* More rounded */
    max-width: 80%;
    word-wrap: break-word; /* Ensure long words wrap */
    line-height: 1.5;
    font-size: 0.95em;
  }
  .kb-message--bot {
    background: #e6e6e6; /* Light grey for bot */
    color: #333;
    align-self: flex-start;
    border-bottom-left-radius: 4px; /* Slight edge for first message */
  }
  .kb-message--user {
    background: #007bff; /* Blue for user */
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 4px; /* Slight edge for last message */
  }
  .kb-message a {
    color: #004d99; /* Link color within bot messages */
    text-decoration: underline;
  }
  .kb-message--user a {
    color: #e0f2ff; /* Link color within user messages */
  }
  /* Markdown specific styles within messages */
  .kb-message strong, .kb-message b { font-weight: bold; }
  .kb-message em, .kb-message i { font-style: italic; }
  .kb-message ul, .kb-message ol { padding-left: 20px; margin: 5px 0; }
  .kb-message li { margin-bottom: 5px; }
  .kb-message pre {
    background-color: #eee;
    padding: 8px;
    border-radius: 5px;
    font-family: 'Fira Code', 'SF Mono', monospace; /* Monospace font for code */
    font-size: 0.85em;
    white-space: pre-wrap;
    word-break: break-all;
    overflow-x: auto; /* Allow horizontal scrolling for code blocks */
  }
  .kb-message code {
    background-color: #e0e0e0;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: 'Fira Code', 'SF Mono', monospace;
    font-size: 0.85em;
  }
  /* For footnote style sources section */
  .kb-message .sources-section {
    font-size: 0.8em;
    margin-top: 15px;
    padding-top: 10px;
    border-top: 1px solid #ddd;
    color: #666;
  }
  .kb-message .sources-section strong {
    color: #333;
  }
  .kb-message .sources-section ol {
    list-style-type: decimal;
    padding-left: 20px;
    margin-top: 5px;
  }
  .kb-message .sources-section ol li {
    margin-bottom: 3px;
  }

  /* Footer/Input */
  .kb-chat-input-container {
    display: flex;
    padding: 10px 15px;
    border-top: 1px solid #eee;
    background-color: #fff;
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
  }
  #kb-chat-input {
    flex-grow: 1;
    border: 1px solid #ddd;
    border-radius: 20px; /* Pill-shaped input */
    padding: 8px 15px;
    outline: none;
    font-size: 1em;
    margin-right: 10px;
    transition: border-color 0.2s ease;
  }
  #kb-chat-input:focus {
    border-color: #007bff;
  }
  .kb-chat-send-btn {
    background: none;
    border: none;
    cursor: pointer;
    color: #007bff; /* Icon color matches primary */
    padding: 5px;
    display: flex; /* Center SVG */
    align-items: center;
    justify-content: center;
    transition: color 0.2s ease;
  }
  .kb-chat-send-btn:hover {
    color: #0056b3;
  }
  .kb-chat-send-btn:disabled {
    color: #ccc;
    cursor: not-allowed;
  }
  .kb-chat-send-btn svg {
    width: 24px;
    height: 24px;
  }

  /* Loading indicator */
  .kb-message.loading::after {
    content: '.';
    animation: loading-dots 1s infinite steps(1, end);
  }
  @keyframes loading-dots {
    0% { content: '.'; }
    33% { content: '..'; }
    66% { content: '...'; }
  }

  /* Media Queries for Responsiveness */
  @media (max-width: 768px) {
    .kb-chat-window {
      width: 90vw; /* Wider on smaller screens */
      height: 70vh; /* Taller on smaller screens */
      bottom: 90px;
      right: 5vw;
      left: 5vw; /* Center horizontally */
      margin: auto;
    }
    .kb-chat-fab-container {
      bottom: 20px;
      right: 20px;
    }
  }
</style>

<!-- JavaScript Logic for Chatbot -->
<script>
  // Utility to render basic Markdown to HTML
  function renderMarkdown(markdownText) {
    let html = markdownText;

    // Convert bold: **text** or __text__ to <strong>text</strong>
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/__([^_]+)__/g, '<strong>$1</strong>');

    // Convert italics: *text* or _text_ to <em>text</em>
    html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');
    html = html.replace(/_([^_]+)_/g, '<em>$1</em>');

    // Convert links: [text](url) to <a href="url" target="_blank" rel="noopener noreferrer">text</a>
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

    // Convert code blocks (multiline)
    html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    // Convert inline code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Handle paragraphs and lists
    // Split by double newline to treat blocks separately.
    const blocks = html.split(/\n\n+/); 

    let processedHtml = blocks.map(block => {
        // Check for lists at the start of a block
        if (block.match(/^\d+\.\s/) || block.match(/^\s*[-*+]\s/)) {
            // If it's the "相关内容出自：" section, wrap it in a div for specific styling
            if (block.startsWith('**相关内容出自：**')) {
                const sourcesContent = block.substring('**相关内容出自：**'.length).trim();
                const listItems = sourcesContent.split('\n').filter(line => line.trim() !== '').map(item => {
                    // Item could be "1. [Title](URL)"
                    return `<li>${item.replace(/^\d+\.\s/, '').trim()}</li>`;
                }).join('');
                return `<div class="sources-section"><strong>相关内容出自：</strong><ol>${listItems}</ol></div>`;
            } else if (block.match(/^\d+\.\s/)) { // Generic ordered list
                const items = block.split('\n').filter(line => line.match(/^\d+\.\s/)).map(item => `<li>${item.replace(/^\d+\.\s/, '').trim()}</li>`).join('');
                return `<ol>${items}</ol>`;
            } else { // Generic unordered list
                const items = block.split('\n').filter(line => line.match(/^\s*[-*+]\s/)).map(item => `<li>${item.replace(/^\s*[-*+]\s/, '').trim()}</li>`).join('');
                return `<ul>${items}</ul>`;
            }
        } 
        // For other blocks, treat as paragraphs and convert single newlines to <br>
        else {
            return `<p>${block.replace(/\n/g, '<br>')}</p>`;
        }
    }).join('');

    // Remove any empty <p> tags that might result from parsing
    processedHtml = processedHtml.replace(/<p><\/p>/g, '');
    
    return processedHtml;
  }

  const kbChatToggleBtn = document.getElementById('kb-chat-toggle-btn');
  const kbChatCloseBtn = document.getElementById('kb-chat-close-btn');
  const kbChatWindow = document.getElementById('kb-chat-window');
  const kbChatInput = document.getElementById('kb-chat-input');
  const kbChatSendBtn = document.getElementById('kb-chat-send-btn');
  const kbChatMessages = document.getElementById('kb-chat-messages');
  const initialBotMessageDiv = kbChatMessages.querySelector('.kb-message--bot');

  const CHAT_WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat'; // Your KB-Chat Worker URL

  // State variable for chat window visibility
  let isChatWindowOpen = false;

  // --- UI Update & Lifecycle Functions ---
  const toggleChatWindow = () => {
    isChatWindowOpen = !isChatWindowOpen;
    if (isChatWindowOpen) {
      kbChatWindow.classList.add('open');
      localStorage.setItem('kbChatOpenState', 'open'); // Save state
      kbChatInput.focus();
    } else {
      kbChatWindow.classList.remove('open');
      localStorage.setItem('kbChatOpenState', 'closed'); // Save state
    }
  };

  const addMessage = (text, sender, isLoading = false) => {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('kb-message');
    messageDiv.classList.add(`kb-message--${sender}`);
    
    if (isLoading) {
        messageDiv.classList.add('loading');
        // Initial text for loading indicator
        messageDiv.textContent = '思考中'; 
    } else {
        messageDiv.innerHTML = renderMarkdown(text); // Render Markdown for actual content
    }
    
    kbChatMessages.appendChild(messageDiv);
    kbChatMessages.scrollTop = kbChatMessages.scrollHeight; // Auto scroll to bottom
    return messageDiv; // Return the message element to update later if loading
  };

  // --- Initial Setup (PC default open, Mobile default closed) ---
  const initializeChatbotState = () => {
    // Initial bot greeting
    initialBotMessageDiv.innerHTML = renderMarkdown('阿弥陀佛，请问有什么可以帮助您？');

    const isMobile = window.innerWidth <= 768; // Define mobile breakpoint
    const savedState = localStorage.getItem('kbChatOpenState');

    if (savedState) {
        // User has a saved preference
        isChatWindowOpen = (savedState === 'open');
    } else {
        // No saved preference, use default based on device type
        isChatWindowOpen = !isMobile;
    }

    if (isChatWindowOpen) {
      kbChatWindow.classList.add('open');
      // On PC, if opened by default, focus input
      if (!isMobile) kbChatInput.focus(); 
    }
  };

  // --- Event Handlers ---
  const askQuestion = async () => {
    const query = kbChatInput.value.trim();
    if (!query) return;

    addMessage(query, 'user');
    kbChatInput.value = '';
    kbChatInput.disabled = true;
    kbChatSendBtn.disabled = true;

    const thinkingMessageDiv = addMessage('思考中', 'bot', true); // Show loading dots

    try {
      const response = await fetch(CHAT_WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query })
      });

      if (!response.ok) {
        throw new Error(`API 请求失败: ${response.statusText}`);
      }

      const data = await response.json();
      thinkingMessageDiv.classList.remove('loading');
      thinkingMessageDiv.innerHTML = renderMarkdown(data.answer); // Update with rendered Markdown answer

    } catch (error) {
      console.error('Chat error:', error);
      thinkingMessageDiv.classList.remove('loading');
      thinkingMessageDiv.innerHTML = renderMarkdown('抱歉，服务出现了一点问题，请稍后再试。');
    } finally {
      kbChatInput.disabled = false;
      kbChatSendBtn.disabled = false;
      kbChatMessages.scrollTop = kbChatMessages.scrollHeight; // Scroll again after final message
      kbChatInput.focus(); // Focus input for next question
    }
  };

  // --- Event Listeners ---
  kbChatToggleBtn.addEventListener('click', toggleChatWindow);
  kbChatCloseBtn.addEventListener('click', toggleChatWindow); // Use toggle for close as well

  kbChatSendBtn.addEventListener('click', askQuestion);
  kbChatInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault(); // Prevent new line in input
      askQuestion();
    }
  });

  // Initialize chat window state on page load
  document.addEventListener('DOMContentLoaded', initializeChatbotState);
</script>