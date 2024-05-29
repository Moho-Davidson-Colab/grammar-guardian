import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export function SignIn() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleClick: () => void = async () => {
    await axios
      .post("http://127.0.0.1:5000/signin", {
        username: username,
        password: password,
      })
      .then((response) => {
        console.log(response);
        if (response.status === 200) {
          sessionStorage.setItem("auth_token", response.data.auth_token);
          navigate("/home");
        }
      })
      .catch((error) => {
        alert(error.response.data);
      });
  };
  return (
    <div>
      <label htmlFor="email">Username: </label>
      <input
        value={username}
        onChange={(event) => setUsername(event.target.value)}
        name="email"
        id="email"
      />
      <label htmlFor="password">Password: </label>
      <input
        value={password}
        onChange={(event) => setPassword(event.target.value)}
        name="password"
        id="password"
      />
      <button onClick={handleClick}>Sign In</button>
    </div>
  );
}
