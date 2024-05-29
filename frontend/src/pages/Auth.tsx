import { Sign } from "crypto";
import { SignUp } from "../components/signUp";
import { SignIn } from "../components/signIn";

export function Auth() {
  return (
    <div>
      <SignUp />
      <SignIn />
    </div>
  );
}
