import { useContext, createContext, useState, useEffect } from "react";
const AuthContext = createContext({
  authUser: null,
  setAuthUser: (authUser: any) => {},
  isAuthenticated: false,
  setIsAuthenticated: (isAuthenticated: boolean) => {},
});

export const useAuth = () => {
  return useContext(AuthContext);
};

const AuthProvider = (props: any) => {
  const [authUser, setAuthUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <AuthContext.Provider
      value={{ authUser, setAuthUser, isAuthenticated, setIsAuthenticated }}
    >
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
