import React from 'react'
import Message from './Message'

export default function InboxView() {
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
        </div>

        <div className='w-2/3 h-full flex flex-col gap-2'>
            <h1 className='h-[8%] font-semibold bg-white text-xl py-2 px-1 rounded-lg'>Change in the webpage</h1>

            <div className='h-[12%] bg-white text-xl py-2 px-1 rounded-lg gap-2 flex'>
                <img className='h-11 rounded-full' src="https://media.licdn.com/dms/image/D4E03AQGykjGV4y553w/profile-displayphoto-shrink_400_400/0/1703073087373?e=1714003200&v=beta&t=h6W18pmmsFNn6PpsXHiXOsTut6aA3QVNP-hZ_0EYT3I" alt="profile picture" />
                <div>
                    <h1>Sergio Franco | <span className='text-xs'>sergio.franco@swiftmail.com</span></h1>
                    <p className='text-xs'>6:54pm, 21/02/2024</p>
                </div>
            </div>

            <div className='h-[80%] bg-white py-2 px-1 rounded-lg gap-2 flex'>
            Hola Sergio gracias por tu ayuda, te puse otra actualización en
            nuestro documento del sitio web: Sitio web IBIO.
            
            Gracias,
            ____________________________________
            Juliana Torres
            Gestora de Comunicaciones
            Departamento de Ingeniería Biomédica
            Carrera 1 Este No.19ª - 40
            Bogotá, Colombia
            https://ingbiomedica.uniandes.edu.co/
            Facebook  |  Instagram  |   Twitter   |   LinkedIn |   YouTube
            </div>
        </div>
    </section>
  )
}
