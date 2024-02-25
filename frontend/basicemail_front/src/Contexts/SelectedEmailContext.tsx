import { createContext, useState } from "react";

interface MessageProps {
    email: string;
    subject: string;
    body: string;
    timestamp: string;
  }

export const selectedEmailContext = createContext({actualEmail: {"email": "no-selected", "subject": "no-selected", "body": "no-selected", "timestamp": "no-selected"}, setActualEmail: (actualView:MessageProps) => {}});

export function SelectedEmailProvider(props:any) {
    const [actualEmail, setActualEmail] = useState({"email": "no-selected", "subject": "no-selected", "body": "no-selected", "timestamp": "no-selected"});
    return (
        <selectedEmailContext.Provider value={{ actualEmail: actualEmail, setActualEmail: setActualEmail }}>
            {props.children}
        </selectedEmailContext.Provider>
    );
}