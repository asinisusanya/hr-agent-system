import { Bot, User } from "lucide-react";

function Header() {
  return (
    <div className="header">

      <div className="header-left">

        <div className="logo-box">
          <Bot size={30} />
        </div>

        <div>
          <h1>HR Multi-Agent System</h1>
          <p>AI-Powered HR Assistant</p>
        </div>

      </div>

      <div className="header-right">

        <div className="online-badge">
          ● System Online
        </div>

        <div className="user-badge">
          <User size={18} />
          User ID: 1
        </div>

      </div>

    </div>
  );
}

export default Header;