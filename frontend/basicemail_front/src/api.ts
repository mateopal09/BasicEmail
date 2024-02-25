import axios from 'axios';

export const getEmails = (curretUser: string) => {
    return axios.get('http://localhost:8000/api/get-email/');
}

export const sendEmail = (subject: string, email: string, body: string) => {
    return axios.post('http://localhost:8000/api/send-email/', { subject, email, body });
}

