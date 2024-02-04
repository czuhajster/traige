import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';

// Define the InjuryCase and InjuryData classes outside of any Widget to ensure they are accessible globally
class InjuryCase {
  final String user_id;
  String status;
  InjuryData data;
  double confidence;

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

// InjuryView StatefulWidget
class InjuryView extends StatefulWidget {
  @override
  _InjuryViewState createState() => _InjuryViewState();
}

class _InjuryViewState extends State<InjuryView> {
  late final WebSocketChannel channel;
  List<InjuryCase> injuryList = []; // injuryList is now a non-static member of _InjuryViewState

  @override
  void initState() {
    super.initState();
    connectWebSocket();
    
  }

  void connectWebSocket() {
    channel = WebSocketChannel.connect(
      Uri.parse('wss://traige-ws.saajan.net/ws'),
    );

    channel.stream.listen((message) {
      print('Received: $message');
      // print('Received: ${message.runes.toList()}');
      processReceivedData(message);
    }, onDone: () {
      print('Channel closed');
    }, onError: (error) {
      print('Websocket Error: $error');
    });
  }

  void processReceivedData(String message) {
    setState(() {
    final jsonData = jsonDecode(message.trim()) as Map<String, dynamic>;
    createCase(jsonData);
      try {
        // final jsonData = jsonDecode(message.trim()) as Map<String, dynamic>;
        // createCase(jsonData);
      } catch (e) {
        print('Error processing received data: $e');
      }
    });
  }

void createCase(Map<String, dynamic> jsonData) {
  String user_id = jsonData['user_ID'];
  InjuryCase? existingCase;

  try {
    existingCase = injuryList.firstWhere(
      (caseItem) => caseItem.user_id == user_id,
    );

        existingCase.status = jsonData['status'];
    existingCase.data = InjuryData(
      bpm: jsonData['data']['bpm'],
      oxygen_saturation: jsonData['data']['oxygen_saturation'],
      diastolic: jsonData['data']['diastolic'],
      systolic: jsonData['data']['systolic'],
    );
    existingCase.confidence = jsonData['confidence'];
  } catch (e) {
        InjuryCase newCase = InjuryCase(
      user_id: user_id,
      status: jsonData['status'],
      data: InjuryData(
        bpm: jsonData['data']['bpm'],
        oxygen_saturation: jsonData['data']['oxygen_saturation'],
        diastolic: jsonData['data']['diastolic'],
        systolic: jsonData['data']['systolic'],
      ),
      confidence: jsonData['confidence'],
    );
    injuryList.add(newCase);
  }

  // if (existingCase != null) {
  //   // Update the existing case...
  //   existingCase.status = jsonData['status'];
  //   existingCase.data = InjuryData(
  //     bpm: jsonData['data']['bpm'],
  //     oxygen_saturation: jsonData['data']['oxygen_saturation'],
  //     diastolic: jsonData['data']['diastolic'],
  //     systolic: jsonData['data']['systolic'],
  //   );
  //   existingCase.confidence = jsonData['confidence'];
  // } else {
  //   // Create a new case and add it to the list...
  // }

  // Sort the list based on confidence, highest first.
  injuryList.sort((a, b) => b.confidence.compareTo(a.confidence));
}


  @override
  void dispose() {
    channel.sink.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Injury List'),
      ),
      body: Center(
        child: ListView.builder(
          padding: const EdgeInsets.all(8),
          itemCount: injuryList.length,
          itemBuilder: (BuildContext context, int index) {
            final item = injuryList[index];
            return ListTile(
              title: Text('Injury ID: ${item.user_id}, Status: ${item.status}, Confidence: ${item.confidence}'),
              subtitle: Text('BPM: ${item.data.bpm}, Saturation: ${item.data.oxygen_saturation}, Diastolic: ${item.data.diastolic}, Systolic: ${item.data.systolic}'),
            );
          },
        ),
      ),
    );
  }
}

void main() => runApp(MaterialApp(home: InjuryView()));
