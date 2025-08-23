---
title: 搜索
excerpt: Search for a page or post you're looking for
---

{% include site-search.html %}



<!-- 聊天按钮 -->
<button id="kb-chat-button" style="position: fixed; bottom: 20px; right: 20px; z-index: 1000; padding: 12px 18px; background-color: #4A90E2; color: white; border: none; border-radius: 50px; cursor: pointer; box-shadow: 0 4px 8px rgba(0,0,0,0.2); font-size: 16px;">
  与 AI 对话
</button>

<!-- 聊天窗口 -->
<div id="kb-chat-window" style="display: none; position: fixed; bottom: 80px; right: 20px; width: 350px; height: 500px; background: white; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); z-index: 1000; display: flex; flex-direction: column;">
  <div style="padding: 15px; background: #4A90E2; color: white; border-top-left-radius: 15px; border-top-right-radius: 15px; font-weight: bold;">
    佛法知识问答
  </div>
  <div id="kb-chat-messages" style="flex-grow: 1; padding: 15px; overflow-y: auto; border-bottom: 1px solid #eee;">
    <!-- 消息会显示在这里 -->
     <div style="background: #f1f1f1; padding: 10px; border-radius: 10px; margin-bottom: 10px; max-width: 80%; align-self: flex-start;">阿弥陀佛，请问有什么问题可以帮您？</div>
  </div>
  <div style="padding: 10px; border-top: 1px solid #ddd;">
    <form id="kb-chat-form" style="display: flex;">
      <input type="text" id="kb-chat-input" placeholder="输入您的问题..." style="flex-grow: 1; border: 1px solid #ccc; border-radius: 20px; padding: 10px 15px; outline: none;">
      <button type="submit" style="margin-left: 10px; background: #4A90E2; color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer;">➤</button>
    </form>
     <!-- Cloudflare Turnstile Widget -->
     <div class="cf-turnstile" data-sitekey="0x4AAAAAABuXOWUyZUiwdrdo" data-callback="onTurnstileSuccess"></div>
  </div>
</div>

<!-- 引入 Turnstile 的脚本 -->
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const chatButton = document.getElementById('kb-chat-button');
  const chatWindow = document.getElementById('kb-chat-window');
  const chatForm = document.getElementById('kb-chat-form');
  const chatInput = document.getElementById('kb-chat-input');
  const messagesContainer = document.getElementById('kb-chat-messages');
  
  let turnstileToken = null;

  // Turnstile 成功验证后的回调函数
  window.onTurnstileSuccess = function(token) {
    turnstileToken = token;
  };

  // 切换聊天窗口显示
  chatButton.addEventListener('click', () => {
    const isHidden = chatWindow.style.display === 'none';
    chatWindow.style.display = isHidden ? 'flex' : 'none';
  });

  // 表单提交事件
  chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = chatInput.value.trim();
    if (!query) return;

    if (!turnstileToken) {
      addMessage("请先完成人机身份验证。", 'ai');
      return;
    }

    addMessage(query, 'user');
    chatInput.value = '';
    addMessage("思考中...", 'ai', true); // 添加加载提示

    try {
      const response = await fetch('https://proxy.true-dhamma.com/kb-chat', { // 替换成你的 kb-chat worker 地址
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: query,
          'cf-turnstile-response': turnstileToken
        })
      });

      const responseText = await response.text();
      updateLastMessage(responseText, 'ai');

      // 每次成功后重置 Turnstile，以便下次提问
      if (window.turnstile) {
        window.turnstile.reset();
        turnstileToken = null;
      }

    } catch (error) {
      console.error('Error:', error);
      updateLastMessage('抱歉，服务出现了一些问题，请稍后再试。', 'ai');
    }
  });

  function addMessage(text, sender, isLoading = false) {
    const messageElement = document.createElement('div');
    messageElement.textContent = text;
    messageElement.style.padding = '10px';
    messageElement.style.borderRadius = '10px';
    messageElement.style.marginBottom = '10px';
    messageElement.style.maxWidth = '80%';
    messageElement.style.wordWrap = 'break-word';

    if (sender === 'user') {
      messageElement.style.background = '#4A90E2';
      messageElement.style.color = 'white';
      messageElement.style.alignSelf = 'flex-end';
    } else {
      messageElement.style.background = '#f1f1f1';
      messageElement.style.color = 'black';
      messageElement.style.alignSelf = 'flex-start';
      if (isLoading) {
        messageElement.id = 'loading-message';
      }
    }
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  function updateLastMessage(text, sender) {
    const loadingMessage = document.getElementById('loading-message');
    if (loadingMessage) {
      loadingMessage.textContent = text;
      loadingMessage.id = ''; // 移除ID，防止下次更新错误
    } else {
      addMessage(text, sender);
    }
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
});
</script>