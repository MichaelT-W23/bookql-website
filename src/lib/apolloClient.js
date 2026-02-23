import { ApolloClient, InMemoryCache } from '@apollo/client';

const graphqlEndpoint = 'https://www.general-api.com/bookql/graphql';

const apolloClient = new ApolloClient({
  uri: graphqlEndpoint,
  cache: new InMemoryCache(),
});

export default apolloClient;
