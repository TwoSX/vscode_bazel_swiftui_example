import DemoModule

final class DemoModuleTests: XCTestCase {
    func test_success() {
        XCTAssertTrue(DemoModule.returnTrue())
    }
}