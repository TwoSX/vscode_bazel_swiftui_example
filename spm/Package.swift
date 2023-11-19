// swift-tools-version: 5.9

import PackageDescription

let package = Package(
  name: "vscode_bazel_swiftui_example",
  platforms: [
    .iOS(.v16)
  ],
  dependencies: [
    .package(url: "https://github.com/krzysztofzablocki/Inject", from: "1.2.4")
  ]
)
