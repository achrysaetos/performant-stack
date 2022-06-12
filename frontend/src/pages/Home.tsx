import { Box, Button } from "@chakra-ui/react";
import useSWR, { useSWRConfig } from "swr";

const fetcher = (url: RequestInfo | URL) =>
  fetch(url).then((res) => res.json());

export default function App() {
  const { data, error } = useSWR("http://localhost:8000/users", fetcher);
  const { mutate } = useSWRConfig();

  if (error) return <div>failed to load</div>;
  if (!data) return <div>loading...</div>;

  function updateFn(user: any): any {
    return user;
  }

  async function createUser() {
    const res = await fetch("http://localhost:8000/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: "aa@aa.com",
        username: "new_user",
        password: "password"
      }),
    });
    const json = await res.json();
    console.log(json);
  }

  async function deleteUser() {
    const res = await fetch("http://localhost:8000/users/28", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id: 28,
      }),
    });
    const json = await res.json();
    console.log(json);
  }

  return (
    <>
      {data.map((user: any) => (
        <Box>Email: {user.email}, Username: {user.username}, Password: {user.password}, Id: {user.id}</Box>
      ))}
      <Button onClick={createUser}>Create a new user</Button>
      <Button onClick={deleteUser}>Delete a user</Button>
    </>
  );
}
