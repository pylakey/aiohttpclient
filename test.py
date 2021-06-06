import asyncio

import pydantic

from paiohttpclient import HttpClient


class Post(pydantic.BaseModel):
    id: int
    title: str
    body: str


class Posts(pydantic.BaseModel):
    __root__: list[Post] = []


class PostsData(pydantic.BaseModel):
    data: Posts


class PostsResponseData(pydantic.BaseModel):
    posts: PostsData


async def main():
    api_client = HttpClient(
        'https://graphqlzero.almansi.me',
        common_headers={
            'ContentType': 'application/json'
        }
    )

    query = """
    {
      posts {
        data {
          id
          title
          body
        }
      }
    }
    """

    response = await api_client.graphql_request(query, path='/api', data_model=PostsResponseData)
    print(response.json(indent=4))
    # {
    #   "data": {
    #     "posts": {
    #       "data": [
    #         {
    #           "id": 1,
    #           "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    #           "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    #         },
    #         {
    #           "id": 2,
    #           "title": "qui est esse",
    #           "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    #         },
    #         <...>
    #         {
    #           "id": 100,
    #           "title": "at nam consequatur ea labore ea harum",
    #           "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
    #         }
    #       ]
    #     }
    #   },
    #   "error": null
    # }


if __name__ == '__main__':
    asyncio.run(main())
