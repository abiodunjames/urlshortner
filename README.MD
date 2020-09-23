# Usage

- Configure `tier.app` hostname 

``` 
echo "127.0.0.1  tier.app localhost" | sudo tee -a /etc/hosts

```
- Create `.env` file at the root folder with this content

```
POSTGRES_USER=user
POSTGRES_DB=tier
POSTGRES_PASSWORD=password
DATABASE_URI='postgresql://user:password@db/tier'
DOMAIN_NAME=http://tier.app
```
- Run `docker-compose up -d --build`

- Check API docs `http://tier.app/docs`

- Get a short url 

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"url":"https://google.com"}' \
  http://tier.app/api/urls
```
- Access a shortened url
  ```
  curl  http://tier.app/GHO97J2Xne0
  
  ```

## Running tests

- Change the `DATABASE_URI` value to `sqlite:///test.db`
- Run tests with `docker-compose exec web pytest .`


