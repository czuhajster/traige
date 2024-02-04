import 'package:dashboard/List.dart';
import 'package:flutter/material.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'dart:async';
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'list.dart';

// void main() {
//   runApp(InjuryView());
// }

// void main() {
//   sortInjuryList();
// }

// void testData() {  
//   Map<String, dynamic> json = {  
//     'user_id': '002',  
//     'status': 'healthy',  
//     'data': {  
//       'bpm': 66,  
//       'oxygen_saturation': 55,  
//       'diastolic': 22,  
//       'systolic': 33,  
//     },  
//   };  
//   String jsonString = jsonEncode(json);  
//   print(jsonString);  
// }

class InjuryView extends StatelessWidget {
  static List<InjuryCase> injuryList = [
    InjuryCase(
      user_id: '001',
      status: 'healthy',
      data: InjuryData(bpm: 60, oxygen_saturation: 50, diastolic: 20, systolic: 30),
      confidence: 10,
    ),
    InjuryCase(
      user_id: '002',
      status: 'dead',
      data: InjuryData(bpm: 0, oxygen_saturation: 0, diastolic: 0, systolic: 0),
      confidence: 100,
    ),
    InjuryCase(
      user_id: '003',
      status: 'unhealthy',
      data: InjuryData(bpm: 66, oxygen_saturation: 55, diastolic: 22, systolic: 33),
      confidence: 50,
    ),
      InjuryCase(
      user_id: '004',
      status: 'healthy',
      data: InjuryData(bpm: 66, oxygen_saturation: 55, diastolic: 22, systolic: 33),
      confidence: 70,
    ),
      InjuryCase(
      user_id: '005',
      status: 'unhealthy',
      data: InjuryData(bpm: 66, oxygen_saturation: 55, diastolic: 22, systolic: 33),
      confidence: 50,
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text('Injury List'),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            Expanded(
              child: ListView.builder(
                padding: const EdgeInsets.all(8),
                itemCount: injuryList.length,
                itemBuilder: (BuildContext context, int index) {
                  return Container(
                    decoration: BoxDecoration(
                      border: Border(
                        bottom: BorderSide(
                          color: Colors.grey,
                          width: 1.0,
                        ),
                      ),
                    ),
                    child: Container(
                      padding: EdgeInsets.all(8),
                      child: InjuryCaseWidget(
                        user_id: injuryList[index].user_id,
                        status: injuryList[index].status,
                        bpm: injuryList[index].data.bpm,
                        oxygen_saturation: injuryList[index].data.oxygen_saturation,
                        diastolic: injuryList[index].data.diastolic,
                        systolic: injuryList[index].data.systolic,
                        confidence: injuryList[index].confidence,
                      ),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}

Future<void> fetchData() async {
  final response = await http.get(Uri.parse('https://api.example.com/data'));

  if (response.statusCode == 200) {
    // Parse the JSON data
    Map<String, dynamic> jsonData = json.decode(response.body);

    print(jsonData);
    // call createCase function
    createCase(jsonData);
    sortInjuryList();
  } else {
    print('Failed to load data. Status code: ${response.statusCode}');
  }
}


InjuryCase? findCaseById(String user_id) {
  try {
    return InjuryView.injuryList.firstWhere((user) => user.user_id == user_id);
  } catch (e) {
    return null;
  }
}

void createCase(jsonData) {
  // Check if the user with user_id exists
  String user_id = jsonData['user_id'];
  String newStatus = jsonData['status'];
  int newBpm = jsonData['bpm'];
  int newOxygen_saturation = jsonData['oxygen_saturation'];
  int newDiastolic = jsonData['diastolic'];
  int newSystolic = jsonData['systolic'];
  int confidence = jsonData['confidence'];
  InjuryCase? existingCase = findCaseById(user_id);

  if (existingCase != null) {
    // Case exists, update the data
    existingCase.status = newStatus;
    existingCase.data.bpm = newBpm;
    existingCase.data.oxygen_saturation = newOxygen_saturation;
    existingCase.data.diastolic = newDiastolic;
    existingCase.data.systolic = newSystolic;
    existingCase.confidence = confidence;
    print('Case updated');
  } else {
    // Case doesn't exist, create a new one
    InjuryCase newCase = InjuryCase(
      user_id: user_id,
      status: newStatus,
      data: InjuryData(
        bpm: newBpm,
        oxygen_saturation: newOxygen_saturation,
        diastolic: newDiastolic,
        systolic: newSystolic,
      ),
      confidence: confidence,
    );
    InjuryView.injuryList.add(newCase);
    print('New case created');
    sortInjuryList();
  }
}

class InjuryCase {
  final String user_id;
  String status;
  InjuryData data;
  int confidence;

  InjuryCase({
    required this.user_id,
    required this.status,
    required this.data,
    required this.confidence,
  });
}

class InjuryData {
  int bpm;
  int oxygen_saturation;
  int diastolic;
  int systolic;

  InjuryData({
    required this.bpm,
    required this.oxygen_saturation,
    required this.diastolic,
    required this.systolic,
  });
}

class InjuryCaseWidget extends StatelessWidget {
  final String user_id;
  String status;
  int bpm;
  int oxygen_saturation;
  int diastolic;
  int systolic;
  int confidence;

  InjuryCaseWidget({
    required this.user_id,
    required this.status,
    required this.bpm,
    required this.oxygen_saturation,
    required this.diastolic,
    required this.systolic,
    required this.confidence,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(5),
      child: Column(
        children: [
          Row(
            children: [
              Icon(Icons.person),
              SizedBox(width: 10), // Add some spacing between the icon and text
              Expanded(
                child: Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    'Injury ID: $user_id, Status: $status Confidence: $confidence',
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                ),
              ),
            ],
          ),
          Align(
            alignment: Alignment.centerLeft,
            child: Text('BPM: $bpm, Saturation: $oxygen_saturation, Diastolic: $diastolic, Systolic: $systolic'),
          ),
        ],
      ),
          );

  }
}


void sortInjuryList() {
  // Custom sorting function based on health status and confidence
  InjuryView.injuryList.sort((a, b) {
    // Sort by health status (unhealthy < healthy < dead)
    int statusComparison = _compareStatus(a.status, b.status);
    if (statusComparison != 0) {
      return statusComparison;
    } else {
      // If status is the same, sort by confidence
      return a.confidence.compareTo(b.confidence);
    }
  });
}

int _compareStatus(String statusA, String statusB) {
  // Define the order: unhealthy comes first, followed by healthy, and then dead
  if (statusA == 'unhealthy' && statusB != 'unhealthy') {
    return -1;
  } else if (statusA != 'unhealthy' && statusB == 'unhealthy') {
    return 1;
  } else if (statusA == 'healthy' && statusB != 'healthy') {
    return -1;
  } else if (statusA != 'healthy' && statusB == 'healthy') {
    return 1;
  } else {
    return 0;
  }
}
