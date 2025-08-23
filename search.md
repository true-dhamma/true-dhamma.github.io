---
title: 搜索
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
    <textarea id="kb-chat-input" placeholder="输入您的问题..." rows="1" autocomplete="off"></textarea>
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
  /* Import Google Fonts for a modern look */
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+SC:wght@400;500;700&display=swap');

  /* FAB Container */
  .kb-chat-fab-container {
    position: fixed;
    bottom: 30px; /* Same as TTS FAB to ensure no conflict, or adjust if needed */
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
    background-color: #4CAF50; /* A soft green for the FAB */
    border-radius: 50%;
    cursor: pointer;
    padding: 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    transition: background-color 0.2s ease-in-out, transform 0.2s ease;
  }
  .kb-chat-fab-button:hover {
    background-color: #45a049; /* Darker green on hover */
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
    border-radius: 12px;
    background: #fff;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3); /* Softer, larger shadow */
    display: flex;
    flex-direction: column;
    overflow: hidden; /* Ensures rounded corners */
    font-family: 'Roboto', 'Noto Sans SC', sans-serif; /* Modern font, with Chinese fallback */
    color: #333;
    z-index: 999; /* Below FAB but above other content */
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); /* Material Design-like curve */
    transform: scale(0.95) translateY(20px); /* Initial subtle offset for animation */
    opacity: 0; /* Initial hidden for animation */
    visibility: hidden; /* For screen readers */
    pointer-events: none; /* Disable interaction when hidden */
  }
  .kb-chat-window.open {
    transform: scale(1) translateY(0);
    opacity: 1;
    visibility: visible;
    pointer-events: auto; /* Enable interaction when open */
  }

  /* Chat Window - Desktop styles */
  @media (min-width: 769px) {
    .kb-chat-window {
      width: 700px; /* Wider window for PC */
      height: 600px; /* Taller window for PC */
      bottom: 100px; /* Position above FAB */
      right: 50%; /* Center horizontally */
      transform: translateX(50%) translateY(20px) scale(0.95); /* Adjust for centering */
    }
    .kb-chat-window.open {
      transform: translateX(50%) translateY(0) scale(1);
    }
  }

  /* Chat Window - Mobile styles */
  @media (max-width: 768px) {
    .kb-chat-window {
      width: 100vw;
      height: 100vh;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      border-radius: 0; /* Full screen, no rounded corners */
      transform: scale(0.95); /* Still animate from smaller */
    }
  }

  /* Header */
  .kb-chat-header {
    background: linear-gradient(to right, #66bb6a, #43a047); /* Softer green gradient */
    color: white;
    padding: 15px 20px;
    font-size: 1.1em;
    font-weight: 500;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Subtle shadow for depth */
  }
  @media (min-width: 769px) {
    .kb-chat-header {
      border-top-left-radius: 12px;
      border-top-right-radius: 12px;
    }
  }
  .kb-chat-close-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 5px;
    margin-right: -5px; /* Adjust to align better visually */
    transition: opacity 0.2s ease;
  }
  .kb-chat-close-btn svg {
    fill: white; /* Close icon color */
    width: 20px;
    height: 20px;
  }
  .kb-chat-close-btn:hover {
    opacity: 0.8;
  }

  /* Messages Container */
  .kb-chat-messages {
    flex-grow: 1;
    overflow-y: auto;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: #fcfcfc; /* Very light background for messages */
  }
  /* Scrollbar styles for modern look */
  .kb-chat-messages::-webkit-scrollbar { width: 8px; }
  .kb-chat-messages::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 10px; }
  .kb-chat-messages::-webkit-scrollbar-thumb { background: #bbb; border-radius: 10px; }
  .kb-chat-messages::-webkit-scrollbar-thumb:hover { background: #999; }

  /* Message Bubbles */
  .kb-message {
    padding: 12px 18px; /* Slightly more padding */
    border-radius: 20px; /* More rounded */
    max-width: 85%; /* Slightly wider */
    word-wrap: break-word; /* Ensure long words wrap */
    line-height: 1.6; /* Better readability */
    font-size: 0.95em;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08); /* Subtle shadow for bubbles */
  }
  .kb-message--bot {
    background: #e9ecef; /* Light grey-blue for bot */
    color: #34495e;
    align-self: flex-start;
    border-bottom-left-radius: 6px; /* Slight edge for first message */
  }
  .kb-message--user {
    background: #d4edda; /* Light green for user */
    color: #214d23;
    align-self: flex-end;
    border-bottom-right-radius: 6px; /* Slight edge for last message */
  }
  .kb-message a {
    color: #007bff; /* Link color within messages */
    text-decoration: underline;
    word-break: break-all; /* Ensure long URLs break */
  }
  .kb-message--user a {
    color: #176d1a; /* Darker green link in user bubbles */
  }
  /* Markdown specific styles within messages */
  .kb-message strong, .kb-message b { font-weight: 700; }
  .kb-message em, .kb-message i { font-style: italic; }
  .kb-message ul, .kb-message ol { padding-left: 25px; margin: 8px 0; }
  .kb-message li { margin-bottom: 4px; }
  .kb-message pre {
    background-color: #f0f0f0;
    padding: 10px;
    border-radius: 6px;
    font-family: 'Fira Code', 'SF Mono', monospace; /* Monospace font for code */
    font-size: 0.8em;
    white-space: pre-wrap;
    word-break: break-all;
    overflow-x: auto; /* Allow horizontal scrolling for code blocks */
    margin-top: 10px;
    margin-bottom: 10px;
    line-height: 1.4;
  }
  .kb-message code {
    background-color: #e0e0e0;
    padding: 2px 5px;
    border-radius: 4px;
    font-family: 'Fira Code', 'SF Mono', monospace;
    font-size: 0.85em;
  }
  /* For footnote style sources section */
  .kb-message .sources-section {
    font-size: 0.85em;
    margin-top: 18px;
    padding-top: 12px;
    border-top: 1px dashed #cfd8dc; /* Dashed line for subtle separation */
    color: #555;
  }
  .kb-message .sources-section strong {
    color: #333;
    display: block; /* Make strong tag a block for better spacing */
    margin-bottom: 5px;
  }
  .kb-message .sources-section ol {
    list-style-type: decimal;
    padding-left: 20px;
    margin-top: 5px;
  }
  .kb-message .sources-section ol li {
    margin-bottom: 3px;
    line-height: 1.4;
  }
  .kb-message p { /* Ensure paragraphs within messages have consistent styling */
    margin: 0;
  }


  /* Footer/Input */
  .kb-chat-input-container {
    display: flex;
    align-items: flex-end; /* Align items to the bottom */
    padding: 10px 15px;
    border-top: 1px solid #eee;
    background-color: #fff;
    box-shadow: 0 -2px 5px rgba(0,0,0,0.05); /* Shadow at bottom */
  }
  @media (min-width: 769px) {
    .kb-chat-input-container {
      border-bottom-left-radius: 12px;
      border-bottom-right-radius: 12px;
    }
  }

  #kb-chat-input {
    flex-grow: 1;
    border: 1px solid #cfd8dc; /* Light, neutral border */
    border-radius: 22px; /* Pill-shaped input */
    padding: 10px 18px; /* More padding */
    outline: none;
    font-size: 1em;
    margin-right: 10px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    resize: none; /* Disable manual resize */
    overflow-y: hidden; /* Hide scrollbar initially */
    min-height: 44px; /* Minimum height for input */
    max-height: 120px; /* Maximum height for input before scrolling */
    line-height: 1.5;
  }
  #kb-chat-input:focus {
    border-color: #66bb6a; /* Green focus highlight */
    box-shadow: 0 0 0 2px rgba(102, 187, 106, 0.2); /* Soft shadow on focus */
  }
  .kb-chat-send-btn {
    background: none;
    border: none;
    cursor: pointer;
    color: #66bb6a; /* Icon color matches primary */
    padding: 8px; /* Larger clickable area */
    display: flex; /* Center SVG */
    align-items: center;
    justify-content: center;
    transition: color 0.2s ease, transform 0.2s ease;
    border-radius: 50%; /* Make button round */
  }
  .kb-chat-send-btn:hover {
    color: #4CAF50;
    transform: scale(1.05);
  }
  .kb-chat-send-btn:disabled {
    color: #bdbdbd; /* Lighter grey when disabled */
    cursor: not-allowed;
    transform: none;
  }
  .kb-chat-send-btn svg {
    width: 24px;
    height: 24px;
  }

  /* Typewriter caret animation */
  .typing-caret {
    display: inline-block;
    width: 2px;
    height: 1.2em; /* Height relative to font size */
    background-color: #333;
    animation: blink-caret 0.75s step-end infinite;
    vertical-align: middle;
    margin-left: 2px;
  }
  @keyframes blink-caret {
    from, to { background-color: transparent; }
    50% { background-color: #333; }
  }
</style>

<!-- JavaScript Logic for Chatbot -->
<script>
  // Utility to render basic Markdown to HTML
  function renderMarkdown(markdownText) {
    if (!markdownText) return '';

    let html = markdownText;

    // Convert bold: **text** or __text__ to <strong>text</strong>
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/__([^_]+)__/g, '<strong>$1</strong>');

    // Convert italics: *text* or _text_ to <em>$1</em>
    html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');
    html = html.replace(/_([^_]+)_/g, '<em>$1</em>');

    // Convert links: [text](url) to <a href="url" target="_blank" rel="noopener noreferrer">text</a>
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

    // Convert code blocks (multiline)
    html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    // Convert inline code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Handle paragraphs and lists
    const blocks = html.split(/\n\n+/); 
    let processedHtml = blocks.map(block => {
        if (!block.trim()) return '';

        // Check for "相关内容出自：" section first
        if (block.startsWith('**相关内容出自：**')) {
            const sourcesContent = block.substring('**相关内容出自：**'.length).trim();
            const listItems = sourcesContent.split('\n').filter(line => line.trim() !== '').map(item => {
                // Each item might be "1. [Title](URL)"
                const parsedItem = item.replace(/^\d+\.\s/, '').trim(); // Remove leading number and dot
                return `<li>${parsedItem}</li>`;
            }).join('');
            return `<div class="sources-section"><strong>相关内容出自：</strong><ol>${listItems}</ol></div>`;
        } 
        // Then handle generic ordered lists
        else if (block.match(/^\d+\.\s/)) {
            const items = block.split('\n').filter(line => line.match(/^\d+\.\s/)).map(item => {
                 const parsedItem = item.replace(/^\d+\.\s/, '').trim();
                 return `<li>${parsedItem}</li>`;
            }).join('');
            return `<ol>${items}</ol>`;
        } 
        // Then handle generic unordered lists
        else if (block.match(/^\s*[-*+]\s/)) {
            const items = block.split('\n').filter(line => line.match(/^\s*[-*+]\s/)).map(item => {
                const parsedItem = item.replace(/^\s*[-*+]\s/, '').trim();
                return `<li>${parsedItem}</li>`;
            }).join('');
            return `<ul>${items}</ul>`;
        }
        // Handle code blocks that might be on their own line
        else if (block.startsWith('<pre><code>')) {
            return block; // Already processed by regex, just return it
        }
        // For everything else, treat as paragraph and convert single newlines to <br>
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
  let isTyping = false;
  const TYPING_SPEED = 20; // Milliseconds per character

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
        messageDiv.textContent = '思考中'; 
    } else {
        // Placeholder for typewriter effect or direct render
    }
    
    kbChatMessages.appendChild(messageDiv);
    kbChatMessages.scrollTop = kbChatMessages.scrollHeight; // Auto scroll to bottom
    return messageDiv; // Return the message element to update later if loading/typing
  };

  const typewriterEffect = (element, markdownText, callback) => {
    isTyping = true;
    const plainText = markdownText.replace(/<\/?[^>]+(>|$)/g, ""); // Remove HTML for typing animation
    let i = 0;
    element.innerHTML = ''; // Clear content for typing

    const caret = document.createElement('span');
    caret.classList.add('typing-caret');
    element.appendChild(caret);

    const type = () => {
      if (i < plainText.length) {
        element.textContent += plainText.charAt(i);
        element.appendChild(caret); // Keep caret at the end
        kbChatMessages.scrollTop = kbChatMessages.scrollHeight;
        i++;
        setTimeout(type, TYPING_SPEED);
      } else {
        isTyping = false;
        caret.remove(); // Remove caret after typing is done
        element.innerHTML = renderMarkdown(markdownText); // Render full markdown after typing
        kbChatMessages.scrollTop = kbChatMessages.scrollHeight;
        if (callback) callback();
      }
    };
    type();
  };

  // --- Initial Setup (PC default open, Mobile default closed) ---
  const initializeChatbotState = () => {
    // Initial bot greeting
    // Use raw markdown for the typewriter effect, then it will be rendered
    const greetingMarkdown = '阿弥陀佛，请问有什么可以帮助您？';
    const initialBotMsgDiv = kbChatMessages.querySelector('.kb-message--bot');
    
    // Set initial text with typewriter effect
    typewriterEffect(initialBotMsgDiv, greetingMarkdown, () => {
      kbChatMessages.scrollTop = kbChatMessages.scrollHeight;
      if (isChatWindowOpen) {
          kbChatInput.focus(); // Only focus if already open
      }
    });

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
    }
  };

  // --- Auto-resize textarea ---
  const autoResizeTextarea = () => {
    kbChatInput.style.height = 'auto'; // Reset height to recalculate
    kbChatInput.style.height = kbChatInput.scrollHeight + 'px'; // Set to scroll height
    kbChatMessages.scrollTop = kbChatMessages.scrollHeight; // Keep chat scrolled
  };

  // --- Event Handlers ---
  const askQuestion = async () => {
    const query = kbChatInput.value.trim();
    if (!query || isTyping) return;

    addMessage(query, 'user');
    kbChatInput.value = '';
    autoResizeTextarea(); // Reset textarea height after sending
    kbChatInput.disabled = true;
    kbChatSendBtn.disabled = true;

    const botMessageDiv = addMessage('思考中', 'bot'); // This will be updated by typewriter
    
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
      typewriterEffect(botMessageDiv, data.answer, () => {
        // Callback after typing is done
        kbChatInput.disabled = false;
        kbChatSendBtn.disabled = false;
        kbChatInput.focus();
        kbChatMessages.scrollTop = kbChatMessages.scrollHeight;
      });

    } catch (error) {
      console.error('Chat error:', error);
      botMessageDiv.innerHTML = renderMarkdown('抱歉，服务出现了一点问题，请稍后再试。');
      kbChatInput.disabled = false;
      kbChatSendBtn.disabled = false;
      kbChatMessages.scrollTop = kbChatMessages.scrollHeight;
      kbChatInput.focus();
    } finally {
      // These are now handled in the typewriter callback or error block
    }
  };

  // --- Event Listeners ---
  kbChatToggleBtn.addEventListener('click', toggleChatWindow);
  kbChatCloseBtn.addEventListener('click', toggleChatWindow); // Use toggle for close as well

  kbChatSendBtn.addEventListener('click', askQuestion);
  kbChatInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !event.shiftKey) { // Allow Shift+Enter for new line
      event.preventDefault(); // Prevent new line in input if only Enter is pressed
      askQuestion();
    }
  });
  // Adjust textarea height on input
  kbChatInput.addEventListener('input', autoResizeTextarea);


  // Initialize chat window state on page load
  document.addEventListener('DOMContentLoaded', initializeChatbotState);
  window.addEventListener('resize', () => {
    // Re-evaluate open state on resize for responsiveness
    const isMobileNow = window.innerWidth <= 768;
    const savedState = localStorage.getItem('kbChatOpenState');

    if (!savedState) { // If no user override, adjust based on device type
      if (isMobileNow && isChatWindowOpen) {
        kbChatWindow.classList.remove('open');
        isChatWindowOpen = false;
      } else if (!isMobileNow && !isChatWindowOpen) {
        kbChatWindow.classList.add('open');
        isChatWindowOpen = true;
      }
    }
    autoResizeTextarea(); // Adjust textarea height if window resized
  });
</script>