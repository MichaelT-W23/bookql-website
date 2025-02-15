import { ApolloClient, InMemoryCache } from '@apollo/client';

const graphqlEndpoint = 'https://api.bookql.com/graphql';

const apolloClient = new ApolloClient({
  uri: graphqlEndpoint,
  cache: new InMemoryCache(),
});

export default apolloClient;