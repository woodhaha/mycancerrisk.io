$scope.model = {};
        $scope.schema = {
            type: "object",
            properties: {
                radios1_1: {
                    title: " Do you consider yourself to be Hispanic or Latino?",
                    type: "string",
                    enum: [
                        1,
                        "No"
                    ]
                },
                radios1_2: {
                    title: " Which of the following do you consider yourself to be?",
                    type: "string",
                    enum: [
                        "White",
                        "Black or African-American",
                        "Asian or Pacific Islander"
                    ]
                },
                select1_1: {
                    title: "What is your age? ",
                    type: "string",
                    enum: [
                        "50","51","52",
                        "53","54","55",
                        "56","57","58",
                        "59","60","61",
                        "62","63","64",
                        "65","66","67",
                        "68","69","70",
                        "71","72","73",
                        "74","75","76",
                        "77","78","79",
                        "80","81","82",
                        "83","84","85"
                    ],
                    description: "NOTE: This tool calculates risk for men and women 50 to 85 years of age."
                },
                radios1_3: {
                    title: " What is your sex?",
                    type: "string",
                    enum: [
                        "Male",
                        "Female"
                    ]
                },
                height_feet: {
                    title: "What is your height without shoes?(feet)",
                    type: "string",
                    enum: [
                        "0","1","2","3","4","5",
                        "6","7","8","9","10","11"
                    ],
                },
                height_inches: {
                    title: "What is your height without shoes?(inches)",
                    type: "string",
                    enum: [
                        "1","2","3","4","5",
                        "6","7","8","9","10","11"
                    ],
                },
                weight: {
                    title: "What is your weight without shoes?(lbs)",
                    type: "number"
                },
                tag: {
                    title: "Tag",
                    type: "string"
                },
                select2_1: {
                    title: "In the past 30 days, about how many servings per week of vegetables or leafy green salads did you eat?",
                    type: "string",
                    enum: [
                        "None",
                        "Less than 1 serving per week",
                        "1-2 servings per week",
                        "3-4 servings per week",
                        "5-6 servings per week",
                        "7-10 servings per week",
                        "More than 10 servings per week",
                    ],
                    description: "NOTE: If you have eaten vegetables in the past 30 days, you will define serving size in the next question."
                },
                select2_2: {
                    title: "In the past 30 days, how much did you usually eat in each serving of vegetables or leafy green salads?",
                    type: "string",
                    enum: [
                        "1/2 cup or less",
                        "Between 1/2 cup and 1 1/2 cups",
                        "Between 1 1/2 cup and 3 cups",
                        "Between 3 cup and 5 cups",
                        "More than 5 cups"
                    ]
                },
                radios3_1: {
                    title: "During the past 10 years, did you have a colonoscopy, sigmoidoscopy, or both?",
                    type: "string",
                    enum: [
                        "Yes",
                        "No",
                        "I don't know"
                    ]
                },
                radios3_2: {
                    title: "In the past 10 years did a healthcare provider tell you that you had a colon or rectal polyp?",
                    type: "string",
                    enum: [
                        "Yes",
                        "No",
                        "I don't know"
                    ]
                },
                radios4_1: {
                    title: "During the past 30 days, have you taken medications containing aspirin at least 3 times a week, such as: Bufferin, Bayer, Excedrin, Other generic form",
                    type: "string",
                    enum: [
                        "Yes",
                        "No",
                        "I don't know"
                    ],
                    description: "NOTE: Do NOT include TYLENOL"
                },
                radios4_2: {
                    title: "During the past 30 days, have you taken medications that do NOT contain aspirin at least 3 times a week, such as: Advil, Aleve, Celebrex, Ibuprofen, Motrin, Naproxen, Nuprin",
                    type: "string",
                    enum: [
                        "Yes",
                        "No",
                        "I don't know"
                    ],
                    description: "NOTE: Do NOT include TYLENOL"
                },
                select5_1: {
                    title: "Over the past 12 months, in how many months, if any, did you do any kind of moderate physical activity?",
                    type: "string",
                    enum: [
                        "1","2","3","4","5","6",
                        "7","8","9","10","11","12"
                    ]
                },
                select5_2: {
                    title: "During those months, on average, about how many hours per week did you do moderate physical activities?",
                    type: "string",
                    enum: [
                        "Up to 1 hour per week",
                        "Between 1-2 hours per week",
                        "Between 2-3 hours per week",
                        "Between 3-4 hours per week",
                        "More than 4 hours per week"
                    ]
                },
                select5_3: {
                    title: "Over the past 12 months, in how many months, if any, did you do any kind of vigorous physical activity?",
                    type: "string",
                    enum: [
                        "1","2","3","4","5","6",
                        "7","8","9","10","11","12"
                    ]
                },
                select5_4: {
                    title: "During those months, on average, about how many hours per week did you do vigorous physical activities?",
                    type: "string",
                    enum: [
                        "Up to 1 hour per week",
                        "Between 1-2 hours per week",
                        "Between 2-3 hours per week",
                        "Between 3-4 hours per week",
                        "More than 4 hours per week"
                    ]
                },
                radios6_1: {
                    title: "Do you still have periods?",
                    type: "string",
                    enum: [
                        "Yes",
                        "No"
                    ]
                },
                select6_1: {
                    title: "When did you have your last period?",
                    type: "string",
                    enum: [
                        "1 year ago or less",
                        "More than 1 year ago but less than 2 years ago",
                        "2 year ago or more"
                    ]
                },
                radios6_2: {
                    title: "During the past 2 years, have you used estrogen, progestin, or other female hormones?",
                    type: "string",
                    enum: [
                        "Yes",
                        "No"
                    ],
                    description: "Note: These hormones may be given as hormone pills, oral contraceptives, shots, skin patches, vaginal creams, or as vaginal suppositories."
                },
                select7_1: {
                    title: "Think only about your biological mother and father, full brothers and sisters, and your biological sons or daughters. At any time in their lives, did any of these relatives ever have cancer of the colon or rectum (cancer of the lower intestine)? ",
                    type: "string",
                    enum: [
                        "Yes",
                        "No",
                        "I don't know"
                    ]
                },
                select7_2: {
                    title: "How many of these relatives had cancer of the colon or rectum (cancer of the lower intestine)?",
                    type: "string",
                    enum: [
                        "1",
                        "2 or more",
                        "I don't know"
                    ]
                },
                switch1: {
                    title: "Continue",
                    type: "boolean"
                },
                switch2: {
                    title: "Continue",
                    type: "boolean"
                },
                switch3: {
                    title: "Continue",
                    type: "boolean"
                },
                switch4: {
                    title: "Continue",
                    type: "boolean"
                },
                switch5: {
                    title: "Continue",
                    type: "boolean"
                },
                switch6: {
                    title: "Continue",
                    type: "boolean"
                }
            }
        };
        $scope.form = [
                      {
                        type: "help",
                        helpvalue: "<h4>Section 1 － Demographics<h4>"
                      },
                      {
                        key: "radios1_1",
                        type: "radios",
                        titleMap: [
                          {
                            value: 1,
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          }
                        ]
                      },
                      {
                        key: "radios1_2",
                        type: "radios",
                        titleMap: [
                          {
                            value: "White",
                            name: "White"
                          },
                          {
                            value: "Black or African-American",
                            name: "Black or African-American"
                          },
                          {
                            value: "Asian or Pacific Islander",
                            name: "Asian or Pacific Islander"
                          }
                        ]
                      },
                      {
                        key: "select1_1",
                        type: "select",
                        titleMap: [
                          { value: "50", name: "50"},{ value: "51", name: "51"},{ value: "52", name: "52"},{ value: "53", name: "53"},{ value: "54", name: "54"},{ value: "55", name: "55"},{ value: "56", name: "56"},{ value: "57", name: "57"},{ value: "58", name: "58"},{ value: "59", name: "59"},
                          { value: "60", name: "60"},{ value: "61", name: "61"},{ value: "62", name: "62"},{ value: "63", name: "63"},{ value: "64", name: "64"},{ value: "65", name: "65"},{ value: "66" ,name: "66"},{ value: "67", name: "67"},{ value: "68", name: "68"},{ value: "69", name: "69"},
                          { value: "70", name: "61"},{ value: "71", name: "71"},{ value: "72", name: "72"},{ value: "73", name: "73"},{ value: "74", name: "74"},{ value: "75", name: "75"},{ value: "76", name: "76"},{ value: "77", name: "77"},{ value: "78", name: "78"},{ value: "79", name: "79"},
                          { value: "80", name: "71"},{ value: "81", name: "71"},{ value: "82", name: "82"},{ value: "83", name: "83"},{ value: "84", name: "84"},{ value: "85", name: "85"}
                        ]
                      },
                      {
                        key: "radios1_3",
                        type: "radios",
                        titleMap: [
                          {
                            value: "Male",
                            name: "Male"
                          },
                          {
                            value: "Female",
                            name: "Female"
                          }
                        ]
                      },
                      {
                            key: "height_feet"
                      },
                      {
                            key: "height_inches"
                      },
                      {
                            key: "weight"
                      },
                      {
                            key: "switch1"
                      },
                      {
                        type: "help",
                        helpvalue: "<h4>Section 2 － Diet<h4>",
                        condition: "model.switch1"
                      },
                    {
                        key: "select2_1",
                        type: "select",
                        titleMap: [
                           { value: "None", name: "None" },
                           { value: "Less than 1 serving per week", name: "Less than 1 serving per week"},
                           { value: "1-2 servings per week", name: "1-2 servings per week"},
                           { value: "3-4 servings per week", name: "3-4 servings per week"},
                           { value: "5-6 servings per week", name: "5-6 servings per week"},
                           { value: "7-10 servings per week", name: "7-10 servings per week"},
                           { value: "More than 10 servings per week", name: "More than 10 servings per week"}
                        ],
                        condition: "model.switch1"
                    },
                    {
                        key: "select2_2",
                        type: "select",
                        titleMap: [
                           { value: "1/2 cup or less", name: "1/2 cup or less"},
                           { value: "Between 1/2 cup and 1 1/2 cups", name: "Between 1/2 cup and 1 1/2 cups"},
                           { value: "Between 1 1/2 cup and 3 cups", name: "Between 1 1/2 cup and 3 cups"},
                           { value: "Between 3 cup and 5 cups", name: "Between 3 cup and 5 cups"},
                           { value: "More than 5 cups", name: "More than 5 cups"}
                        ],
                        condition: "model.switch1"
                    },
                    {
                        key: "switch2",
                        condition: "model.switch1"
                    },
                    {
                        type: "help",
                        helpvalue: "<h4>Section 3 － Medical History<h4>",
                        condition: "model.switch2"
                    },
                    {
                        key: "radios3_1",
                        type: "radios",
                        titleMap: [
                          {
                            value: "Yes",
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          },
                          {
                            value: "I don't know",
                            name: "I don't know"
                          }
                        ],
                        condition: "model.switch2"
                    },
                    {
                        key: "radios3_2",
                        type: "radios",
                        titleMap: [
                          {
                            value: "Yes",
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          },
                          {
                            value: "I don't know",
                            name: "I don't know"
                          }
                        ],
                        condition: "model.switch2"
                    },
                    {
                        key: "switch3",
                        condition: "model.switch2"
                    },
                    {
                        type: "help",
                        helpvalue: "<h4>Section 4 － Medications<h4>",
                        condition: "model.switch3"
                    },
                    {
                        key: "radios4_1",
                        type: "radios",
                        titleMap: [
                          {
                            value: "Yes",
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          },
                          {
                            value: "I don't know",
                            name: "I don't know"
                          }
                        ],
                        condition: "model.switch3"
                    },
                    {
                        key: "radios4_2",
                        type: "radios",
                        titleMap: [
                          {
                            value: "Yes",
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          },
                          {
                            value: "I don't know",
                            name: "I don't know"
                          }
                        ],
                        condition: "model.switch3"
                    },
                    {
                        key: "switch4",
                        condition: "model.switch3"
                    },
                    {
                        type: "help",
                        helpvalue: "<h4>Section 5 － Physical Activity<h4>",
                        condition: "model.switch4"
                    },
                    {
                        key: "select5_1",
                        type: "select",
                        titleMap: [
                           { value: "1", name: "1"},{ value: "2", name: "2"},{ value: "3", name: "4"},{ value: "4", name: "4"},
                           { value: "5", name: "5"},{ value: "6", name: "6"},{ value: "7", name: "7"},{ value: "8", name: "8"},
                           { value: "9",name: "9"},{ value: "10",name: "10"},{ value: "11",name: "11"},{ value: "12",name: "12"}
                        ],
                        condition: "model.switch4"
                    },
                    {
                        key: "select5_2",
                        type: "select",
                        titleMap: [
                           { value: "Up to 1 hour per week", name: "Up to 1 hour per week"},
                           { value: "Between 1-2 hours per week", name: "Between 1-2 hours per week"},
                           { value: "Between 2-3 hours per week", name: "Between 2-3 hours per week"},
                           { value: "Between 3-4 hours per week", name: "Between 3-4 hours per week"},
                           { value: "More than 4 hours per week", name: "More than 4 hours per week"}
                        ],
                        condition: "model.switch4"
                    },
                    {
                        key: "select5_3",
                        type: "select",
                        titleMap: [
                           { value: "1", name: "1"},{ value: "2", name: "2"},{ value: "3", name: "4"},{ value: "4", name: "4"},
                           { value: "5", name: "5"},{ value: "6", name: "6"},{ value: "7", name: "7"},{ value: "8", name: "8"},
                           { value: "9",name: "9"},{ value: "10",name: "10"},{ value: "11",name: "11"},{ value: "12",name: "12"}
                        ],
                        condition: "model.switch4"
                    },
                    {
                        key: "select5_4",
                        type: "select",
                        titleMap: [
                           { value: "Up to 1 hour per week", name: "Up to 1 hour per week"},
                           { value: "Between 1-2 hours per week", name: "Between 1-2 hours per week"},
                           { value: "Between 2-3 hours per week", name: "Between 2-3 hours per week"},
                           { value: "Between 3-4 hours per week", name: "Between 3-4 hours per week"},
                           { value: "More than 4 hours per week", name: "More than 4 hours per week"}
                        ],
                        condition: "model.switch4"
                    },
                    {
                        key: "switch5",
                        condition: "model.switch4"
                    },
                    {
                        type: "help",
                        helpvalue: "<h4>Section 6 － Miscellaneous<h4>",
                        condition: "model.switch5"
                    },
                    {
                        key: "radios6_1",
                        type: "radios",
                        titleMap: [
                          {
                            value: "Yes",
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          }
                        ],
                        condition: "model.switch5"
                    },
                    {
                        key: "select6_1",
                        type:"select",
                        titleMap: [
                          {
                            value: "1 year ago or less",
                            name: "1 year ago or less"
                          },
                          {
                            value: "More than 1 year ago but less than 2 years ago",
                            name: "More than 1 year ago but less than 2 years ago"
                          },
                          {
                            value: "2 year ago or more",
                            name: "2 year ago or more"
                          }
                        ],
                        condition: "model.switch5"
                    },
                    {
                        key: "radios6_2",
                        type: "radios",
                        titleMap: [
                          {
                            value: "Yes",
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          }
                        ],
                        condition: "model.switch5"
                    },
                    {
                        key: "switch6",
                        condition: "model.switch5"
                    },
                    {
                        type: "help",
                        helpvalue: "<h4>Section 7 － Family<h4>",
                        condition: "model.switch6"
                    },
                    {
                        key: "select7_1",
                        type:"select",
                        titleMap: [
                          {
                            value: "Yes",
                            name: "Yes"
                          },
                          {
                            value: "No",
                            name: "No"
                          },
                          {
                            value: "I don't know",
                            name: "I don't know"
                          }
                        ],
                        condition: "model.switch6"
                    },
                    {
                        key: "select7_2",
                        type:"select",
                        titleMap: [
                          {
                            value: "1",
                            name: "1"
                          },
                          {
                            value: "2 or more",
                            name: "2 or more"
                          },
                          {
                            value: "I don't know",
                            name: "I don't know"
                          }
                        ],
                        condition: "model.switch6"
                    },
                    {
                        type: "submit",
                        style: "btn btn-default",
                        title: "submit",
                        onClick: "onSubmit",
                        condition: "model.switch6"
                    }

         ];