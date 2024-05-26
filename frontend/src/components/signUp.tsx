import { useState } from "react";
import axios from "axios";

export function SignUp() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleClick: () => void = async () => {
    await axios
      .post("http://127.0.0.1:5000/signup", {
        username: username,
        password: password,
      })
      .then((response) => {
        console.log(response);
        if (response.status === 201) {
          sessionStorage.setItem("access_token", response.data.access_token);
          document.cookie = `refresh_token=${response.data.refresh_token}`;
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
      <button onClick={handleClick}>Sign up</button>
    </div>
  );
}
