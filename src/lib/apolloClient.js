import { ApolloClient, InMemoryCache } from '@apollo/client';

const graphqlEndpoint = 'http://127.0.0.1:8000/graphql';

const apolloClient = new ApolloClient({
  uri: graphqlEndpoint,
  cache: new InMemoryCache(),
});

export default apolloClient;