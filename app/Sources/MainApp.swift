import SwiftUI

#if DEBUG
@_exported import Inject
#endif

@main
struct MainApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
