const VideoData = [
    {
      name: "Miss Scarlet",
      present: true,
      rooms: [
        { kitchen: false },
        { ballroom: false },
        { conservatory: false },
        { "dining room": false },
        { "billiard room": false },
        { library: false },
      ],
    },
    {
      name: "Mrs. White",
      present: false,
      rooms: [
        { kitchen: false },
        { ballroom: false },
        { conservatory: false },
        { "dining room": false },
        { "billiard room": false },
        { library: false },
      ],
    },
    {
      name: "Reverend Green",
      present: true,
      rooms: [
        { kitchen: false },
        { ballroom: false },
        { conservatory: false },
        { "dining room": false },
        { "billiard room": false },
        { library: false },
      ],
    },
    {
      name: "Rusty",
      present: false,
      rooms: [
        { kitchen: false },
        { ballroom: false },
        { conservatory: false },
        { "dining room": false },
        { "billiard room": false },
        { library: false },
      ],
    },
  ];
  
  /**
   * We are going to want to filter by those who were present, but first
   * we need to write our filter function.
   *
   * For this, we using _.filter()
   *
   * _.filter(arr, callback) {
   *  // return when it is found true
   * }
   */
  
  const _ = {};
  
  _.filter = function (list, callback) {
    const storage = [];
  
    // for (let i = 0; i < list.length; i++) {
    //   if (callback(list[i], i, list) === true) {
    //     storage.push(list[i]);
    //   }
    // }
  
    _.each(list, function (item, i, list) {
      console.log(callback.toString()); // 
      if (callback(item, i, list) === true) {
        storage.push(item);
      }
    });
  
    return storage;
  };
  
  _.each = function (list, callback) {
    if (Array.isArray(list)) {
      for (let i = 0; i < list.length; i++) {
        console.log(callback.toString())
        callback(list[i], i, list);
      }
    } else {
      for (let key in list) {
        callback(list[key], key, list);
      }
    }
  };
  
  const out = _.filter(VideoData, (value) => {
    return value.present === true;
  });
  
  // console.log(out);
  