import React from 'react'
import Message from './Message'

export default function ComposeView() {
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
            <input placeholder='Subject...' className='h-[8%] font-semibold bg-white text-xl py-2 px-1 rounded-lg'></input>

            <input placeholder='Email...' type='email' className='h-[12%] bg-white text-xl py-2 px-1 rounded-lg gap-2 flex'>
                
            </input>

            <input placeholder='Body...' type='text' className='h-[80%] bg-white py-2 px-1 rounded-lg gap-2 flex'>
            
            </input>

            <button className='bg-white rounded-md'>Sumbit</button>
        </div>
    </section>
  )
}
