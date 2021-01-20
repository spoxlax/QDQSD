import React, {useState, useEffect} from 'react';
import axios from "axios";
import * as Constant from './const'


const Emails = () => {
    const [mail, setMail] = useState({list: []});

    useEffect(() => {
        const fetchData = async () => {
            const queryResult = await axios.post(
                Constant.GraphQL_Api, {query: Constant.Query}
            );
            const result = queryResult.data.data;
            setMail({list: result.users})
            console.log(result)
        };
        fetchData()

    }, [])


    return (
        <div>
            <ul>
                {
                    mail.list.map(em => (
                        <div key={em.id}>
                            <li> {em.email} </li>
                            <li> {em.firstName} </li>
                            <li> {em.lastName} </li>
                        </div>
                        // <li key={em.id}> {em.} </li>
                    ))
                }
            </ul>
        </div>
    );
}

export default Emails;
