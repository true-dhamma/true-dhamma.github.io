---
title: 搜索
excerpt: Search for a page or post you're looking for
---

{% include site-search.html %}

<!-- Markdown Renderer CDN -->
<!-- Marked.js 是一个高性能的 Markdown 解析器，用于将 Markdown 文本转换为 HTML。 -->
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>

<!-- Chat Widget Styles -->
<style>
  /* 从您的网站 CSS 中提取的基础颜色和样式，以保持一致性 */
  :root {
    --primary-text-color: #34495e; /* 主要文本颜色 */
    --header-color: #2c3e50; /* 标题颜色，也用于按钮背景 */
    --link-color: #3a77d8; /* 链接颜色 */
    --link-hover-color: #2e60ad; /* 链接悬停颜色 */
    --border-color: #e0e0e0; /* 通用边框颜色 */
    --input-bg-color: #fff; /* 输入框背景 */
    --input-placeholder-color: #a8adac; /* 输入框占位符颜色 */
    --send-button-bg: var(--header-color); /* 发送按钮背景，与标题色一致 */
    --send-button-hover-bg: #3a4f65; /* 发送按钮悬停颜色 */
    --bot-message-bg: #eef; /* 机器人消息背景（淡蓝色） */
    --user-message-bg: #dcf8c6; /* 用户消息背景（淡绿色） */
    --chat-header-bg: #f4f6f8; /* 聊天框头部背景（淡灰色，来自 .feature background） */
    --chat-message-area-bg: #fcfcfc; /* 聊天消息区域背景（略微偏白的灰色） */

    /* 为 rgba() 效果定义颜色的 RGB 值 */
    --link-color-rgb: 58, 119, 216;
    --header-color-rgb: 44, 62, 80;
  }

  /* 通用盒模型设置 */
  .chat-widget * {
    box-sizing: border-box;
  }

  /* 浮动输入框样式 */
  #chat-floating-input {
    position: fixed;
    bottom: 100px; /* 离底部约 100px */
    right: 20px;
    width: 280px; /* PC 端宽度 */
    max-width: calc(100% - 40px); /* 手机端宽度，两侧留 20px 边距 */
    background: var(--input-bg-color);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15); /* 柔和阴影 */
    z-index: 1000; /* 确保在最上层 */
    display: flex;
    align-items: center;
    padding: 8px 12px;
    box-sizing: border-box;
    cursor: pointer; /* 指示可点击 */
    transition: transform 0.2s ease-out, opacity 0.2s ease-out; /* 动画效果 */
  }

  #chat-floating-input:hover {
    box-shadow: 0 6px 16px rgba(0,0,0,0.2); /* 悬停时增强阴影 */
    transform: translateY(-2px); /* 向上微移 */
  }

  #chat-floating-input input {
    flex-grow: 1;
    border: none;
    outline: none;
    font-size: 1rem;
    color: var(--primary-text-color);
    padding: 0;
    background: transparent;
    cursor: pointer; /* 保持输入框可点击 */
  }

  #chat-floating-input input::placeholder {
    color: var(--input-placeholder-color);
  }
  
  /* 聊天框外背景遮罩层 */
  #chat-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0,0,0,0.4); /* 半透明黑色 */
    z-index: 999; /* 在浮动输入框之下，聊天框之上 */
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease-out, visibility 0s 0.3s; /* 动画效果 */
  }

  #chat-overlay.open {
    opacity: 1;
    visibility: visible;
    transition: opacity 0.3s ease-out, visibility 0s; /* 打开时立即显示 */
  }

  /* 完整聊天窗口样式 */
  #chat-full-window {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 90vw; /* PC 端宽度为视口宽度的 90% */
    height: 80vh; /* PC 端高度为视口高度的 80% */
    max-width: 600px; /* PC 端最大宽度 */
    max-height: 700px; /* PC 端最大高度 */
    transform: translate(-50%, -50%) scale(0.95); /* 初始略微缩小并居中 */
    opacity: 0;
    visibility: hidden;
    background: var(--input-bg-color);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25); /* 较强阴影 */
    z-index: 1001; /* 确保在最顶层 */
    display: flex;
    flex-direction: column;
    transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55), opacity 0.3s ease-out, visibility 0s 0.3s; /* 弹性动画 */
  }

  #chat-full-window.open {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
    visibility: visible;
    transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55), opacity 0.3s ease-out, visibility 0s;
  }

  /* 聊天框头部 */
  #chat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 15px;
    background: var(--chat-header-bg);
    border-bottom: 1px solid var(--border-color);
    border-top-left-radius: 12px;
    border-top-right-radius: 12px;
    color: var(--chat-title-color);
    font-weight: 600;
    font-size: 1.1rem;
  }

  #chat-header button {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--input-placeholder-color); /* 柔和的关闭按钮颜色 */
    padding: 0 5px;
    line-height: 1;
    transition: color 0.2s ease-in-out;
  }

  #chat-header button:hover {
    color: var(--header-color); /* 悬停时变深 */
  }

  /* 聊天消息区域 */
  #chat-messages-full {
    flex-grow: 1;
    overflow-y: auto;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    background-color: var(--chat-message-area-bg);
    line-height: 1.6;
    scroll-behavior: smooth; /* 平滑滚动 */
  }

  /* 消息气泡样式 */
  .chat-message {
    padding: 10px 14px;
    border-radius: 18px; /* 更现代的圆角 */
    max-width: 85%;
    word-wrap: break-word;
    box-shadow: 0 1px 2px rgba(0,0,0,0.08); /* 柔和阴影 */
    position: relative;
    font-size: 0.95rem; /* 气泡内文本略小 */
  }

  .bot-message {
    background: var(--bot-message-bg);
    align-self: flex-start;
    border-bottom-left-radius: 4px; /* 一角略尖 */
    color: var(--primary-text-color);
  }

  .user-message {
    background: var(--user-message-bg);
    align-self: flex-end;
    border-bottom-right-radius: 4px; /* 一角略尖 */
    color: var(--primary-text-color);
  }

  /* 打字动画指示器 */
  .thinking-message {
    background: var(--bot-message-bg);
    align-self: flex-start;
    border-bottom-left-radius: 4px;
    color: var(--primary-text-color);
    padding: 10px 14px;
    border-radius: 18px;
    max-width: 85%;
    font-size: 0.95rem;
  }
  .thinking-message::after {
    content: '.';
    animation: typing-dots 1.5s infinite steps(3, end); /* 3步动画 */
  }
  @keyframes typing-dots {
    0%, 20% { content: '.'; }
    40% { content: '..'; }
    60%, 100% { content: '...'; }
  }


  /* 聊天输入框容器（完整窗口） */
  #chat-input-container-full {
    display: flex;
    padding: 10px 15px;
    border-top: 1px solid var(--border-color);
    background: var(--chat-header-bg); /* 与头部背景一致 */
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
  }

  #chat-input-full {
    flex-grow: 1;
    border: 1px solid var(--border-color);
    border-radius: 20px; /* 完全圆角输入框 */
    padding: 8px 15px;
    outline: none;
    font-size: 1rem;
    color: var(--primary-text-color);
    background: var(--input-bg-color);
    transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
  }

  #chat-input-full:focus {
    border-color: var(--link-color); /* 聚焦时高亮 */
    box-shadow: 0 0 0 2px rgba(var(--link-color-rgb), 0.2); /* 柔和的聚焦光晕 */
  }

  #chat-send-button {
    border: none;
    background: var(--send-button-bg);
    color: white;
    padding: 8px 18px;
    border-radius: 20px; /* 完全圆角按钮 */
    margin-left: 10px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 500;
    transition: background 0.2s ease-in-out, opacity 0.2s ease-in-out;
  }

  #chat-send-button:hover:not(:disabled) {
    background: var(--send-button-hover-bg);
  }

  #chat-send-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  /* Markdown 内部元素样式（确保在聊天气泡内正确渲染） */
  .chat-message p:last-child { margin-bottom: 0; } /* 移除消息中最后一个 p 标签的额外底部边距 */
  .chat-message p { margin-top: 0.5em; margin-bottom: 0.5em; } /* 调整段落间距 */
  .chat-message ul, .chat-message ol { padding-left: 20px; margin-top: 0.5em; margin-bottom: 0.5em; }
  .chat-message li { margin-bottom: 0.2em; }
  .chat-message strong { font-weight: 700; color: var(--header-color); } /* 加粗文本 */
  .chat-message em { font-style: italic; } /* 斜体文本 */
  .chat-message a { color: var(--link-color); text-decoration: underline; } /* 链接 */
  .chat-message a:hover { color: var(--link-hover-color); }
  .chat-message code { 
    background-color: rgba(var(--header-color-rgb), 0.1); 
    padding: 2px 4px; 
    border-radius: 4px; 
    font-family: monospace; 
    font-size: 0.85em; 
    white-space: pre-wrap; /* 允许代码内换行 */
    word-break: break-all; /* 强制长单词换行 */
  }
  .chat-message pre { 
    background-color: var(--fafafa); 
    padding: 10px; 
    border-radius: 5px; 
    overflow-x: auto; 
    margin-top: 1em; 
    margin-bottom: 1em; 
    line-height: 1.4;
  }
  .chat-message blockquote {
    border-left: 4px solid var(--border-color);
    padding-left: 10px;
    margin: 1em 0;
    color: var(--primary-text-color);
    font-style: italic;
  }

  /* 手机端适配 */
  @media (max-width: 768px) {
    #chat-floating-input {
      bottom: 70px; /* 手机端离底部更近 */
      right: 15px;
      width: calc(100% - 30px); /* 手机端宽度占满 */
      padding: 6px 10px;
    }
    #chat-floating-input input {
      font-size: 0.95rem;
    }

    #chat-full-window {
      width: 100vw; /* 手机端宽度全屏 */
      height: 100vh; /* 手机端高度全屏 */
      border-radius: 0; /* 手机端取消圆角 */
      top: 0;
      left: 0;
      transform: translate(0, 0) scale(0.95); /* 手机端不进行 translate，只处理 scale */
      transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55), opacity 0.3s ease-out, visibility 0s 0.3s;
    }
    #chat-full-window.open {
      transform: translate(0, 0) scale(1);
    }

    #chat-header {
      padding: 10px 12px;
      font-size: 1rem;
      border-top-left-radius: 0;
      border-top-right-radius: 0;
    }
    #chat-header button {
      font-size: 1.3rem;
    }
    #chat-messages-full {
      padding: 12px;
      gap: 10px;
    }
    .chat-message {
      padding: 8px 12px;
      font-size: 0.9rem;
    }
    #chat-input-container-full {
      padding: 8px 12px;
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
    }
    #chat-input-full, #chat-send-button {
      padding: 6px 12px;
      font-size: 0.9rem;
    }
  }
</style>

<!-- Chat Widget HTML -->
<div class="chat-widget">
  <!-- 默认浮动输入框 -->
  <div id="chat-floating-input">
    <input type="text" id="chat-initial-input" placeholder="向我提问..." />
  </div>

  <!-- 聊天框外背景遮罩层 -->
  <div id="chat-overlay"></div>

  <!-- 完整的聊天窗口 -->
  <div id="chat-full-window">
    <div id="chat-header">
      <span id="chat-title">佛法问答</span>
      <button id="chat-close-button" aria-label="关闭聊天">&times;</button> <!-- Unicode '×' 作为关闭图标 -->
    </div>
    <div id="chat-messages-full">
      <div class="bot-message chat-message">阿弥陀佛，请问有什么可以帮助您？</div>
    </div>
    <div id="chat-input-container-full">
      <input type="text" id="chat-input-full" placeholder="输入您的问题..." />
      <button id="chat-send-button" disabled>发送</button>
    </div>
  </div>
</div>

<!-- Chat Widget JavaScript -->
<script>
  // Cloudflare Worker URL
  const WORKER_URL = 'https://proxy.true-dhamma.com/kb-chat';

  // DOM 元素获取
  const chatFloatingInput = document.getElementById('chat-floating-input');
  const chatInitialInput = document.getElementById('chat-initial-input');
  const chatFullWindow = document.getElementById('chat-full-window');
  const chatOverlay = document.getElementById('chat-overlay');
  const chatCloseButton = document.getElementById('chat-close-button');
  const chatMessagesFull = document.getElementById('chat-messages-full');
  const chatInputFull = document.getElementById('chat-input-full');
  const chatSendButton = document.getElementById('chat-send-button');

  // --- 辅助函数 ---

  // Markdown 渲染函数
  const renderMarkdown = (markdownText) => {
    // 设置 marked.js 选项
    marked.setOptions({
        gfm: true, // 启用 GitHub Flavored Markdown
        breaks: true, // 将换行符转换为 <br>
        // highlight: function(code, lang) { // 可选：代码高亮
        //   const hljs = window.hljs; // 如果您有引入 highlight.js
        //   if (hljs && lang && hljs.getLanguage(lang)) {
        //     try {
        //       return hljs.highlight(code, { language: lang }).value;
        //     } catch (__) {}
        //   }
        //   return code;
        // }
    });
    // 使用 marked.parse 将 Markdown 文本解析为 HTML
    return marked.parse(markdownText || '');
  };

  // 打字机效果函数（带 Markdown 渲染）
  async function typewriterEffect(element, markdownText, speed = 20) { // 调整速度以获得更平滑的效果
    let i = 0;
    element.innerHTML = ''; // 清空现有内容

    // 逐字符显示，并实时渲染整个已显示内容的 Markdown
    while (i < markdownText.length) {
      const currentText = markdownText.substring(0, i + 1);
      element.innerHTML = renderMarkdown(currentText);
      chatMessagesFull.scrollTop = chatMessagesFull.scrollHeight; // 自动滚动到底部
      await new Promise(resolve => setTimeout(resolve, speed)); // 暂停一段时间
      i++;
    }
  }

  // --- UI 状态管理 ---

  // 打开聊天窗口
  function openChat() {
    chatFloatingInput.style.display = 'none'; // 隐藏浮动输入框
    chatFullWindow.classList.add('open'); // 添加 'open' 类以显示聊天窗口
    chatOverlay.classList.add('open'); // 显示遮罩层
    
    // 将浮动输入框中的内容转移到完整聊天框的输入框
    if (chatInitialInput.value.trim() !== '') {
        chatInputFull.value = chatInitialInput.value;
        chatInitialInput.value = ''; // 清空浮动输入框
    }
    chatInputFull.focus(); // 聚焦到完整聊天框的输入框
    toggleSendButtonState(); // 更新发送按钮状态
  }

  // 关闭聊天窗口
  function closeChat() {
    chatFullWindow.classList.remove('open'); // 移除 'open' 类以隐藏聊天窗口
    chatOverlay.classList.remove('open'); // 隐藏遮罩层
    chatFloatingInput.style.display = 'flex'; // 显示浮动输入框
    chatInitialInput.value = ''; // 清空浮动输入框内容
  }

  // 根据输入框内容启用/禁用发送按钮
  function toggleSendButtonState() {
    chatSendButton.disabled = chatInputFull.value.trim() === '';
  }

  // --- 事件监听器 ---

  // 浮动输入框聚焦或点击时打开聊天
  chatFloatingInput.addEventListener('click', openChat);
  chatInitialInput.addEventListener('focus', openChat); // 确保通过 Tab 键聚焦也能打开

  // 关闭聊天按钮和遮罩层点击事件
  chatCloseButton.addEventListener('click', closeChat);
  chatOverlay.addEventListener('click', closeChat);

  // 监听完整聊天框输入框的输入事件，更新发送按钮状态
  chatInputFull.addEventListener('input', toggleSendButtonState);

  // 发送消息函数
  async function sendMessage() {
    const query = chatInputFull.value.trim();
    if (!query) return;

    // 显示用户的问题
    const userMessageDiv = document.createElement('div');
    userMessageDiv.classList.add('user-message', 'chat-message');
    userMessageDiv.innerHTML = renderMarkdown(query); // 用户消息直接渲染 Markdown
    chatMessagesFull.appendChild(userMessageDiv);
    
    chatInputFull.value = ''; // 清空输入框
    toggleSendButtonState(); // 禁用发送按钮
    chatSendButton.textContent = '思考中...'; // 显示思考中状态
    chatSendButton.disabled = true;

    // 显示思考指示器
    const thinkingMessageDiv = document.createElement('div');
    thinkingMessageDiv.classList.add('bot-message', 'chat-message', 'thinking-message');
    chatMessagesFull.appendChild(thinkingMessageDiv);
    chatMessagesFull.scrollTop = chatMessagesFull.scrollHeight; // 滚动到底部

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
      
      // 移除思考指示器
      chatMessagesFull.removeChild(thinkingMessageDiv);

      // 显示机器人回复，使用打字机效果
      const botMessageDiv = document.createElement('div');
      botMessageDiv.classList.add('bot-message', 'chat-message');
      chatMessagesFull.appendChild(botMessageDiv);
      await typewriterEffect(botMessageDiv, data.answer); // 打字机效果

    } catch (error) {
      // 错误处理
      if (thinkingMessageDiv.parentNode === chatMessagesFull) {
          thinkingMessageDiv.classList.remove('thinking-message');
          thinkingMessageDiv.textContent = '抱歉，服务出现了一点问题，请稍后再试。';
      } else {
          // 如果 thinkingMessageDiv 已经被移除（比如在打字机效果前出错了），则创建新的错误消息
          const errorMessageDiv = document.createElement('div');
          errorMessageDiv.classList.add('bot-message', 'chat-message');
          errorMessageDiv.textContent = '抱歉，服务出现了一点问题，请稍后再试。';
          chatMessagesFull.appendChild(errorMessageDiv);
      }
      console.error('Chat error:', error);
    } finally {
      chatSendButton.disabled = false; // 启用发送按钮
      chatSendButton.textContent = '发送'; // 恢复按钮文本
      chatMessagesFull.scrollTop = chatMessagesFull.scrollHeight; // 滚动到底部
      chatInputFull.focus(); // 保持焦点在输入框
    }
  }

  // 完整聊天框的发送按钮点击和回车键事件
  chatSendButton.addEventListener('click', sendMessage);
  chatInputFull.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !chatSendButton.disabled) {
      event.preventDefault(); // 阻止默认的回车换行行为
      sendMessage();
    }
  });

  // 页面加载时，确保浮动输入框可见且可交互
  chatFloatingInput.style.display = 'flex';
  // 如果输入框有预填充内容（例如浏览器自动填充），则更新按钮状态
  toggleSendButtonState();


</script>