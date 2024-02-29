import axios from 'axios';

export const getEmails = (currentUser: string) => {
    return axios.get('http://localhost:8000/api/recieve-email/' + currentUser);
}

export const postEmail = (subject: string, email: string, body: string) => {
    return axios.post('http://localhost:8000/api/send-email/', { "recipient_email": email, "subject": subject, "body": body });
}

export const getUser = (email: string, password: string) => {
    return axios.post('http://localhost:8000/api/login/', { "email": email, "password": password });
}

export const postUser = (email: string, password: string, fullname: string) => {
    return axios.post('http://localhost:8000/api/register/', { "email": email, "password": password, "fullname": fullname });
}

export const getPicture = () => {
    const picturesList = axios.get('https://picsum.photos/v2/list') ;
    return picturesList;
}