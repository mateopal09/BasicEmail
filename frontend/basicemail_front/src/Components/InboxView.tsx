import { useState, useEffect, useContext } from 'react'
import Message from './Message'
import { getEmails } from '../api';
import { selectedEmailContext } from '../Contexts/SelectedEmailContext';

export default function InboxView() {

    const [emails, setEmails] = useState([]);
    const falseEmails = [{"subject": "Subject1", "email": "email1", "body": "body1", "timestamp": "timestamp1"}]

    const { actualEmail, setActualEmail } = useContext(selectedEmailContext);

    async function getEmailsEffect() {
        const data = await getEmails("sergio.franco@swiftmail.com");
        setEmails(data.data);
    }

    useEffect(() => {
        //getEmailsEffect();
    }, []);

    return (
        <section className='
        w-2/3 
        h-full
        rounded-xl
        backdrop-blur bg-white/30
        border border-white
        p-6 gap-2
        flex'>
            <div className='w-1/3 h-full gap-5 flex flex-col items-center text-white'>
                {falseEmails.map((actualEmail: any) => {
                    return (
                        <div>
                            <button onClick={() => setActualEmail(actualEmail)}><Message {...actualEmail}  /></button>
                            <hr className='w-3/4' />
                        </div>
                    );
                })}
                {/*
                
                <Message />
                <hr className='w-3/4' />
                <Message />
                <hr className='w-3/4' />
                <Message />
                <hr className='w-3/4' />
                <Message />
                <hr className='w-3/4' />
                <Message />
                <hr className='w-3/4' />
                <Message />
                */}    
            </div>

            {actualEmail.subject == "no-selected" ? (
                <div>Select an email to view it</div>
            ) : (
                <div className='w-2/3 h-full flex flex-col gap-2'>
                    <h1 className='h-[8%] font-semibold bg-white text-xl py-2 px-1 rounded-lg'>{actualEmail.subject}</h1>

                    <div className='h-[12%] bg-white text-xl py-2 px-1 rounded-lg gap-2 flex'>
                        <img className='h-11 rounded-full' src="https://media.licdn.com/dms/image/D4E03AQGykjGV4y553w/profile-displayphoto-shrink_400_400/0/1703073087373?e=1714003200&v=beta&t=h6W18pmmsFNn6PpsXHiXOsTut6aA3QVNP-hZ_0EYT3I" alt="profile picture" />
                        <div>
                            <h1>Sergio Franco | <span className='text-xs'>{actualEmail.email}</span></h1>
                            <p className='text-xs'>{actualEmail.timestamp}</p>
                        </div>
                    </div>

                    <div className='h-[80%] bg-white py-2 px-1 rounded-lg gap-2 flex'>
                        {actualEmail.body}
                    </div>
                </div>
            )}


        </section>
    )
}
