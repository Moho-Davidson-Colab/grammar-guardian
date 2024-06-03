import React, { useState } from "react";
import { SignUp } from "../components/signUp";
import { SignIn } from "../components/signIn";
import Test from "../components/login";
import Register from "../components/register";
import { Button, Container, Box } from "@mui/material";

export function Auth() {
  const [showSignIn, setShowSignIn] = useState(true);

  const toggleView = () => {
    setShowSignIn(!showSignIn);
  };

  return (
    <Container>
      <Box display="flex" justifyContent="center" mt={2}>
        <Button variant="contained" onClick={toggleView}>
          {showSignIn ? "Switch to Sign Up" : "Switch to Sign In"}
        </Button>
      </Box>
      {showSignIn ? <Test /> : <Register />}
    </Container>
  );
}
