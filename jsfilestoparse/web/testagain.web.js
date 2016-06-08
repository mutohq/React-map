// Import Statements
import React, {
    Component
} from 'react';
import {
    AppRegistry,
    StyleSheet,
    Text,
    View,
    NavigatorIOS
} from 'react-native';

// Include Any Pages
var SearchPage = require('./SearchPage');



// Class App
class HelloWorld extends Component {
    render() {
        return ( <span style={styles.container}>
            <p style={styles.name}>
            Hello, Bhavyanth!
            </p> </span>
			/*<TouchableHighlight style={styles.button}
            onPress={this.onSearchPressed.bind(this)}
            underlayColor='#99d9f4'>
          <span style={styles.buttonp}>Go</span>
        </TouchableHighlight>*/


        );
    }
}

class PropertyFinder extends Component {
    render() {
        return ( <span>
            </span>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#F5FCFF',
    },
    containerNav: {
        flex: 1
    },
    name: {
        fontSize: 20,
        textAlign: 'center',
        margin: 10,
    },
    location: {
        textAlign: 'center',
        color: '#333333',
        marginBottom: 5,
    },
});

AppRegistry.registerComponent('PropertyFinder', () => PropertyFinder);
