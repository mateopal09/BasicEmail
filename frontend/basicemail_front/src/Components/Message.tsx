import React, { Attributes } from 'react'

interface MessageProps {
  email: string;
  subject: string;
  body: string;
  timestamp: string;
}

export default function Message({subject, email, body, timestamp}: MessageProps) {
  return (
    <article className='w-full flex items-center gap-2'>
        <img className='h-11 rounded-full' src="https://media.licdn.com/dms/image/D4E03AQGykjGV4y553w/profile-displayphoto-shrink_400_400/0/1703073087373?e=1714003200&v=beta&t=h6W18pmmsFNn6PpsXHiXOsTut6aA3QVNP-hZ_0EYT3I" alt="profile picture" />
        <div>
            <h1 className='text-base font-bold'>Sergio Franco <span className='text-[10px] font-normal'>{timestamp}</span></h1>
            <p className='text-sm'>{subject}</p>
        </div>
    </article>
  )
}
