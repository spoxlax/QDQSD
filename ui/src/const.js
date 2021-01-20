// import axios from "axios";

export const GraphQL_Api = "http://localhost:8000/graphql";
export const Query = `{
  users{
    id
    firstName
    lastName
    email
  }
}`




// axios(
//     {
//         url: 'http://localhost:8000/graphql',
//         method: 'post',
//         data: {
//             query: `{
//   users{
//     id
//     firstName
//     lastName
//     email
//   }
// }`
//         }
//     }
// )
//     .then(res => {
//         // console.log(res.data.data);
//         setMail(res.data.data);
//     })
//     //             res => { this.setState({mail : res.data});
//     //                 // console.log(res.data.json()
//     //             )
//     // })
//     .catch(err => {
//         console.log(err.message);
//     });
// console.log(mail)