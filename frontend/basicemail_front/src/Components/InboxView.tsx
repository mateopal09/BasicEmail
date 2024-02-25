import { useState, useEffect, useContext } from 'react'
import Message from './Message'
import { getEmails } from '../api';
import { selectedEmailContext } from '../Contexts/SelectedEmailContext';
import EmailIcon from '../Icons/EmailIcon';

export default function InboxView() {

    const [emails, setEmails] = useState([]);
    const falseEmails = [{"subject": "Subject1", "email": "email1@swiftmail.com", "body": "body1", "timestamp": "1:46PM 12/12/2021"},
                        {"subject": "Subject2", "email": "email2@swiftmail.com", "body": "body2", "timestamp": "12:46PM 12/12/2021"},
                        {"subject": "Subject3", "email": "email3@swiftmail.com", "body": "body3", "timestamp": "12:46PM 12/12/2021"},
                        {"subject": "Subject4", "email": "email4@swiftmail.com", "body": "body4", "timestamp": "11:46PM 12/12/2021"},
                        {"subject": "Subject5", "email": "email5@swiftmail.com", "body": "body5", "timestamp": "10:46PM 12/12/2021"},
                        {"subject": "Subject6", "email": "email6@swiftmail.com", "body": "body6", "timestamp": "9:46PM 12/12/2021"}]

    const { actualEmail, setActualEmail } = useContext(selectedEmailContext);

    async function getEmailsEffect() {
        const data = await getEmails("remitente@example.com");
        setEmails(data.data);
    }

    useEffect(() => {
        getEmailsEffect();
        console.log(emails)
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
                {emails.map((actualEmail: any) => {
                    return (
                        <div className='gap-5 items-center flex flex-col'>
                            <Message {...actualEmail} />
                            <hr className='w-3/4 animate-[fadein_0.5s]' />
                        </div>
                    );
                })} 
            </div>

            {actualEmail.subject == "no-selected" ? (
                <div className='bg-white w-2/3 h-full rounded-xl flex flex-col items-center place-content-center animate-[fadein_0.5s]'>
                    <EmailIcon />
                    <h1 className='font-bold text-xl'>Seleccione un elemento para leerlo</h1>
                    <p>No hay nada seleccionado</p>

                </div>
            ) : (
                <div className='w-2/3 h-full flex flex-col gap-2'>
                    <h1 className='animate-[fadein_0.5s] h-[8%] font-semibold bg-white text-xl py-2 px-1 rounded-lg'>{actualEmail.subject}</h1>

                    <div className=' animate-[fadein_0.5s] h-[12%] bg-white text-xl py-2 px-1 rounded-lg gap-2 flex'>
                        <img className='h-11 rounded-full' src="https://media.licdn.com/dms/image/D4E03AQGykjGV4y553w/profile-displayphoto-shrink_400_400/0/1703073087373?e=1714003200&v=beta&t=h6W18pmmsFNn6PpsXHiXOsTut6aA3QVNP-hZ_0EYT3I" alt="profile picture" />
                        <div className='animate-[fadein_0.5s]'>
                            <h1>Sergio Franco | <span className='text-xs'>{actualEmail.email}</span></h1>
                            <p className='text-xs'>{actualEmail.timestamp}</p>
                        </div>
                    </div>

                    <div className='animate-[fadein_0.5s] h-[80%] bg-white py-2 px-1 rounded-lg gap-2 flex'>
                        {actualEmail.body}
                    </div>
                </div>
            )}


        </section>
    )
}
