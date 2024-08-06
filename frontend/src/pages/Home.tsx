import { useEffect } from "react";
import axios from "axios";

export function Home() {
  let value = `; ${document.cookie}`;
  let parts = value.split(`; refresh_token=`)!;
  let refresh_token = parts.pop()?.split(";").shift();

  useEffect(() => {
    const refreshToken = async () =>
      await axios
        .post("http://127.0.0.1:5000/refresh", {
          access_token: sessionStorage.getItem("access_token"),
          refresh_token: refresh_token,
        })
        .then((response) => {
          console.log(response);
          if (response.status === 200) {
            sessionStorage.setItem("access_token", response.data.access_token);
            document.cookie = `refresh_token=${response.data.refresh_token}`;
          }
        })
        .catch((error) => {
          alert(error.response.data);
        });

    refreshToken();
  }, []);

  return <div>HomePage</div>;
}
