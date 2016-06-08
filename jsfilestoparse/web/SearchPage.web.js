import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  TextInput,
  TouchableHighlight,
  ActivityIndicatorIOS,
  Image,
  View,
  NavigatorIOS
} from 'react-native';

var SearchResults = require('./SearchResults');

// Query Function
function urlForQueryAndPage(key, value, pageNumber) {
  var data = {
      country: 'uk',
      pretty: '1',
      encoding: 'json',
      listing_type: 'buy',
      action: 'search_listings',
      page: pageNumber
  };
  data[key] = value;
 
  var querystring = Object.keys(data)
    .map(key => key + '=' + encodeURIComponent(data[key]))
    .join('&');
 
  return 'http://api.nestoria.co.uk/api?' + querystring;
};


class SearchPage extends Component {
  // --- Set the initial state object, which is used as a key value store
  constructor(props) {
  super(props);
  this.state = {
    searchString: 'london',
    isLoading: false,
    message: ''
  };
  }
  // Event Handler
  onSearchTextChanged(event) {
    this.setState({ searchString: event.nativeEvent.text });
  }

  _executeQuery(query) {
  console.log(query);
  this.setState({ isLoading: true });

  // Can be used instead of XMLHttpRequest
  fetch(query)
  .then(response => response.json())
  .then(json => this._handleResponse(json.response))
  .catch(error =>
     this.setState({
      isLoading: false,
      message: 'Something bad happened ' + error
   }));
  }

  _handleResponse(response) {
    this.setState({ isLoading: false , message: '' });
    console.log("RESPONSE CODE"+response.application_response_code);
    if (response.application_response_code.substr(0, 1) === '1') {
      this.props.navigator.push({
      title: 'Results',
      component: SearchResults,
      passProps: {listings: response.listings}
      });

    } else {
      this.setState({ message: 'Location not recognized; please try again.'});
    }
  }

  

  onSearchPressed() {
  var query = urlForQueryAndPage('place_name', this.state.searchString, 1);
  this._executeQuery(query);
  }

  render(){
    //console.log('SearchPage.render');
    var spinner = this.state.isLoading ?
    ( <ActivityIndicatorIOS size='large'/> ) :
    ( <View/>);

    return(
      <span style={styles.container}>

        <p style={styles.description}>
          Search for houses to buy!
        </p>
        <p style={styles.description}>
          Search by place-name, postcode or search near your location.
        </p>

        <span style={styles.flowRight}>
        /*<TextInput
          style={styles.searchInput}
          value={this.state.searchString}
          onChange={this.onSearchTextChanged.bind(this)}
          placeholder='Search via name or postcode'/>*/

        /*<TouchableHighlight style={styles.button}
            onPress={this.onSearchPressed.bind(this)}
            underlayColor='#99d9f4'>
          <p style={styles.buttonp}>Go</p>
        </TouchableHighlight>*/*/
        </span>

        /*<TouchableHighlight style={styles.button}
          underlayColor='#99d9f4'>
        <p style={styles.buttonp}>Location</p>
        </TouchableHighlight>*/*/
        /*<Image source={require('./Resources/house.png')} style={styles.image}/>*/
        {spinner}
        <p style={styles.description}>{this.state.message}</p>


      </span>



      );
  }
}


const styles = StyleSheet.create({
  description: {
    marginBottom: 20,
    fontSize: 18,
    textAlign: 'center',
    color: '#656565'
  },
  container: {
    padding: 30,
    marginTop: 65,
    alignItems: 'center'
  },
  flowRight: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'stretch'
  },
  buttonText: {
    fontSize: 18,
    color: 'white',
    alignSelf: 'center'
  },
  button: {
    height: 36,
    flex: 1,
    flexDirection: 'row',
    backgroundColor: '#48BBEC',
    borderColor: '#48BBEC',
    borderWidth: 1,
    borderRadius: 8,
    marginBottom: 10,
    alignSelf: 'stretch',
    justifyContent: 'center'
  },
  searchInput: {
  height: 36,
  padding: 4,
  marginRight: 5,
  flex: 4,
  fontSize: 18,
  borderWidth: 1,
  borderColor: '#48BBEC',
  borderRadius: 8,
  color: '#48BBEC'
},
  image: {
    width: 217,
    height: 138
  },

  }
);

module.exports = SearchPage;

AppRegistry.registerComponent('PropertyFinder', () => PropertyFinder);
