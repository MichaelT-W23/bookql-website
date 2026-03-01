import { ApolloClient, InMemoryCache } from '@apollo/client';

const graphqlEndpoint = 'https://www.general-api.com/bookql/graphql';

const apolloClient = new ApolloClient({
  uri: graphqlEndpoint,
  cache: new InMemoryCache(),
});

export default apolloClient;


// import { ApolloClient, InMemoryCache, HttpLink } from '@apollo/client/core';

// const httpLink = new HttpLink({
//   uri: 'https://www.general-api.com/bookql/graphql',
// });

// const apolloClient = new ApolloClient({
//   link: httpLink,
//   cache: new InMemoryCache(),
// });

// export default apolloClient;