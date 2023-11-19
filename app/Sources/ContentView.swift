import SwiftUI
import DemoModule

#if DEBUG
  import Inject
#endif

struct ContentView: View {
  var body: some View {
    VStack {
      Text("hello world")

      // 一个地球图标
      Image(systemName: "globe")
        .resizable()
        .frame(width: 100, height: 100)
        .padding()

      // 一个按钮
      Button("hello world") {
        DemoModule.printHello()
      }
    }.enableInjection()
  }

  #if DEBUG
    @ObserveInjection var inject
  #endif
}
