import { createContext, useState } from "react";

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const ActualViewContext = createContext({actualView: "Inbox", setActualView: (_actualView:string) => {}});

export function ActualViewProvider(props:any) {
  const [actualView, setActualView] = useState("Inbox");
  return (
    <ActualViewContext.Provider value={{ actualView, setActualView }}>
      {props.children}
    </ActualViewContext.Provider>
  );
}