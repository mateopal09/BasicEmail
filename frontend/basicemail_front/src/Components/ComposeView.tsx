import React from 'react'
import Message from './Message'
import {sendEmail} from '../api'
import { useForm } from 'react-hook-form'

export default function ComposeView() {

  const { register, handleSubmit } = useForm()
  const onSubmit = handleSubmit(
    async data => {
      try {
        await sendEmail(data.subject, data.email, data.body)
      } catch (error) {
        console.error('Failed to send email', error)
      }
    }
  )


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

        <form onSubmit={onSubmit}  className='w-2/3 h-full flex flex-col gap-2'>
            <input {...register("subject")} name='subject'  placeholder='Subject...' className='h-[8%] font-semibold bg-white text-xl py-2 px-1 rounded-lg'/>
            <input {...register("email")} name='email' placeholder='Email...' type='email' className='h-[12%] bg-white text-xl py-2 px-1 rounded-lg gap-2 flex'/>
            <textarea {...register("body")} name='body' placeholder='Body...' className='h-[80%] bg-white py-2 px-1 rounded-lg gap-2 flex'/>
            <button className='bg-white rounded-md'>Sumbit</button>
        </form>
    </section>
  )
}
