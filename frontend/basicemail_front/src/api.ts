import axios from 'axios';

export const getEmails = (curretUser: string) => {
    return axios.get('http://localhost:8000/queries/api/v1/queries/');
}

export const sendEmail = ({ subject, email, body }: { subject: string, email: string, body: string }) => {
    return axios.post('http://localhost:8000/queries/api/v1/queries/', { subject, email, body });
}

