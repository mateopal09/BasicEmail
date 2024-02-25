import React, { Attributes, useEffect } from 'react'
import { useContext } from 'react';
import { selectedEmailContext } from '../Contexts/SelectedEmailContext';


interface MessageProps {
  email: string;
  subject: string;
  body: string;
  timestamp: string;
}

export default function Message({subject, email, body, timestamp}: MessageProps) {

  const [isSelected, setIsSelected] = React.useState(false);
  const { actualEmail, setActualEmail } = useContext(selectedEmailContext);

  function clickHandler() {
    setActualEmail({subject, email, body, timestamp});
  }

  useEffect(() => {
    if (actualEmail.subject == subject) {
      setIsSelected(true);
    } else {
      setIsSelected(false);
    }
  }, [actualEmail]);

  return (
    <button onClick={() => clickHandler()} className={`w-full flex items-center gap-2 animate-[leftappear_0.5s] transition p-3 rounded-xl ${isSelected ? 'bg-[#5858B9] hover:bg-[#5858B9]': 'bg-transparent hover:bg-[#dedede] hover:text-black'}`}>
        <img className='h-11 rounded-full' src="https://media.licdn.com/dms/image/D4E03AQGykjGV4y553w/profile-displayphoto-shrink_400_400/0/1703073087373?e=1714003200&v=beta&t=h6W18pmmsFNn6PpsXHiXOsTut6aA3QVNP-hZ_0EYT3I" alt="profile picture" />
        <div>
            <h1 className='text-base font-bold'>Sergio Franco <span className='text-[10px] font-normal'>{timestamp}</span></h1>
            <p className='text-sm text-left'>{subject}</p>
        </div>
    </button>
  )
}
