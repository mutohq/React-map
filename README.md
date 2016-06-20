# React-map

##Python script that maps React Components to platform native (Web, iOS, and Android) components.

##Set up 
* Install python or python3 `sudo apt-get install idle-python3.4`
* Install pip3 `sudo apt-get install python3-pip`

##Instructions
* Put the files to parse in [React-map/jsfilestoparse/input_type_folder] (https://github.com/mutohq/React-map/tree/master/jsfilestoparse) 
* Configure dictionary in [React-map/Dictionary/Storage.json] (https://github.com/mutohq/React-map/blob/master/Dictionary/storage.json)
* Path and Mapping type of input file  is set in [React-map/config.json] (https://github.com/mutohq/React-map/blob/master/config.json)
* After this run `python3 reactmap.py config.json`


## Input type 
* let input file is of ios type in [ios] (https://github.com/mutohq/React-map/tree/master/jsfilestoparse/ios) 
```
return ( <View style = {styles.container}>
            <Text style ={styles.name}>
            Hello, Bhavyanth!
            </Text> </View> 
			<Nav />
			<App />


        );
```


## Ouput 
* then gerated output will be
* 1. [Android] (https://github.com/mutohq/React-map/blob/master/jsfilestoparse/android/index.android.js)
```
    return ( /*<View style = {styles.container}>
            /*<Text style ={styles.name}>
            Hello, Bhavyanth!
            </Text>*/ </View>*/ 
			/*<Nav />*/
			/*<App />*/


        );
```
  
* 2. [Web] (https://github.com/mutohq/React-map/blob/master/jsfilestoparse/web/index.web.js)

```
    return ( <span style = {styles.container}>
            <p style ={styles.name}>
            Hello, Bhavyanth!
            </p> </span> 
			/*<Nav />*/
			/*<App />*/


        );
```

## Dictionary used 
[Dictionary] (https://github.com/mutohq/React-map/blob/master/Dictionary/storage.json)