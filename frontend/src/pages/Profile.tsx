import React from "react";
import { useAuth } from "../contexts/AuthContext";

export function Profile() {
  const { authUser, setAuthUser, isAuthenticated, setIsAuthenticated } =
    useAuth();

  if (!isAuthenticated) {
    return <h1>Not authenticated</h1>;
  } else {
    return (
      <div>
        <h1>Profile</h1>
      </div>
    );
  }
}
