import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';

const Map<String, Color> statusColors = {
  'Healthy': Colors.green,
  'Wounded': Color.fromARGB(255, 244, 133, 54),
  'Deceased': Color.fromARGB(255, 0, 0, 0),
};

const Map<String, int> statusPriority = {
  'Wounded': 1,
  'Healthy': 2,
  'Deceased': 3,
};

const Color defaultStatusColor = Colors.grey;

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


void sortInjuryList() {
  injuryList.sort((a, b) {
    // Compare status priorities first
    int statusCompare = statusPriority[a.status]!.compareTo(statusPriority[b.status]!);

    if (statusCompare != 0) {
      return statusCompare; // If statuses are different, sort by status priority
    } else {
      // If statuses are the same, sort by confidence, highest first
      return b.confidence.compareTo(a.confidence);
    }
  });
}

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
    sortInjuryList();
      try {
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
  sortInjuryList();

  // Sort the list based on confidence, highest first.
  injuryList.sort((a, b) => b.confidence.compareTo(a.confidence));
}


  @override
  void dispose() {
    channel.sink.close();
    super.dispose();
  }

Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(
      backgroundColor: Theme.of(context).colorScheme.primary,
      title: const Text('Squad 1'),
    ),
    body: ListView.builder(
      padding: const EdgeInsets.all(8),
      itemCount: injuryList.length,
      itemBuilder: (BuildContext context, int index) {
        final item = injuryList[index];
        // Ensure the status text is colored according to the user's status
        // Use `toLowerCase()` to match the map keys exactly
        Color statusColor = statusColors[item.status] ?? defaultStatusColor;

        return Card(
          elevation: 4.0,
          margin: const EdgeInsets.symmetric(vertical: 8.0),
          child: ListTile(
            title: Text(
              'Name: ${item.user_id}',
              style: TextStyle(color: Theme.of(context).colorScheme.onSurface),
            ),
            subtitle: Text(
              'BPM: ${item.data.bpm}, Saturation: ${item.data.oxygen_saturation}, Diastolic: ${item.data.diastolic}, Systolic: ${item.data.systolic}',
              style: TextStyle(color: Theme.of(context).colorScheme.onSurface),
            ),
            isThreeLine: true,
            trailing: Row(
              mainAxisSize: MainAxisSize.min, // Limit the row size to its content
              children: [
                Text(
                  item.status,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: statusColor, // Apply the dynamic color to the status text
                  ),
                ),
                SizedBox(width: 8), // Space between text and icon
                Icon(
                  Icons.health_and_safety,
                  color: statusColor, // Apply the dynamic color to the icon
                ),
              ],
            ),
          ),
        );
      },
    ),
  );
}



}

void main() => runApp(MaterialApp(home: InjuryView()));
