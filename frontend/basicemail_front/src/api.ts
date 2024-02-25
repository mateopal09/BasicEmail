import axios from 'axios';

export const getEmails = (currentUser: string) => {
    return axios.get('http://localhost:8000/api/recieve-email/' + currentUser);
}

export const sendEmail = (subject: string, email: string, body: string) => {
    return axios.post('http://localhost:8000/api/send-email/', { "recipient_email": email, "subject": subject, "body": body });
}