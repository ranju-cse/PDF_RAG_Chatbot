css = """
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}

.chat-message.user {
    background-color: #2b313e;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 100%;
    padding: 0 1.5rem;
    color: #fff;
}
</style>
"""


bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.magnific.com/premium-psd/confident-cartoon-businesswoman-portrait_1216555-1048.jpg?semt=ais_hybrid&w=740&q=80"
             style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""


user_template = """
<div class="chat-message user">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbbbvPhxrw5EdbEuN6WfrG3nD2DBEQn9C6Gak4RPuYNjYiPbMt6ZGfkxQ&s=10"
             style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""