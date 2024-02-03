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

  class InjuryView extends StatelessWidget {
    final List<InjuryItem> injuryList = [
      InjuryItem(name: 'Person A', ranking: 3),
      InjuryItem(name: 'person B', ranking: 1),
      InjuryItem(name: 'Person C', ranking: 2),
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
                    child: ListTile(
                      title: Text(injuryList[index].name),
                      subtitle: Text('Priority: ${injuryList[index].ranking}'),
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

//   return ListView.builder(
//     padding: const EdgeInsets.all(8),
//     itemCount: injuryList.length,
//     itemBuilder: (BuildContext context, int index) {
//       return Container(
//         height: 50,
//         color: Colors.amber,
//         child: Center(child: Text('Entry ${injuryList[index]}')),
//       );
//     }
//   );
// }
//   }

class InjuryItem {
  String name;
  int ranking;
  InjuryItem({required this.name, required this.ranking});
}

List<InjuryItem> injuryList = [
  InjuryItem(name: 'Person A', ranking: 3),
  InjuryItem(name: 'person B', ranking: 1),
  InjuryItem(name: 'Person C', ranking: 2),
];

// ListView.builder(
//   itemCount: injuryList.length,
//   itemBuilder: (BuildContext context, int index) {
//     return InjuryListItemWidget(data: injuryList[index]);
//   },
// )

