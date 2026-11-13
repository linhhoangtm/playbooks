# Chọn công nghệ làm mobile app

Cập nhật: 2026-11-13

Không có công nghệ mobile “tốt nhất”, chỉ có công nghệ hợp với team, loại app và ngân sách. Năm 2026, với đa số team nhỏ, lựa chọn thực tế là **Flutter** hoặc **React Native**, tùy team đang quen Dart hay TypeScript. Native và Kotlin Multiplatform hợp khi cần tích hợp sâu với hệ điều hành hoặc đã có sẵn code Android/iOS. Tình trạng từng công nghệ được kiểm tra theo tài liệu chính thức tới tháng 11/2026 (xem mục Nguồn).

## Mục lục

- [1. Chọn nhanh](#1-chọn-nhanh)
- [2. Các lựa chọn hiện nay](#2-các-lựa-chọn-hiện-nay-112026)
- [3. So sánh theo tiêu chí](#3-so-sánh-theo-tiêu-chí)
- [4. Yếu tố quyết định](#4-yếu-tố-quyết-định)
- [5. Khi code cùng AI](#5-khi-code-cùng-ai-claude-code-copilot)
- [6. Build, phát hành và cập nhật](#6-build-phát-hành-và-cập-nhật)
- [7. Gợi ý theo loại app và prompt mẫu](#7-gợi-ý-theo-loại-app-và-prompt-mẫu)
- [Nguồn](#nguồn)

## 1. Chọn nhanh

| Tình huống của bạn | Nên chọn |
| --- | --- |
| Team quen Flutter/Dart, cần một codebase cho iOS + Android (có thể thêm web, desktop) | **Flutter** |
| Team giỏi React/TypeScript, muốn dùng chung kiến thức và một phần code với web | **React Native + Expo** |
| Đã có app Android viết bằng Kotlin, muốn làm thêm iOS dần dần | **Kotlin Multiplatform** (chia sẻ logic, UI native hoặc Compose Multiplatform) |
| App cần tích hợp sâu với hệ điều hành (widget, Apple Watch, CarPlay, AR, xử lý media nặng), có ngân sách cho 2 team | **Native**: Swift/SwiftUI + Kotlin/Jetpack Compose |
| Team C#/.NET, app nội bộ doanh nghiệp dùng hệ sinh thái Microsoft | **.NET MAUI** |
| Đã có web app, cần lên store nhanh, ít tính năng native | **Capacitor** (Ionic) |
| Công cụ hoặc nội dung đơn giản, không cần lên store | **PWA** (web app cài được) |

## 2. Các lựa chọn hiện nay (11/2026)

Theo phân tích của [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/cross-platform-mobile-development) dựa trên khảo sát Stack Overflow, Flutter và React Native là hai framework đa nền tảng phổ biến nhất, nhiều người dùng hơn tất cả các framework khác cộng lại. Cordova/Ionic đang thu hẹp, còn Kotlin Multiplatform đang tăng trưởng. Theo số liệu Appfigures trong cùng bài, khoảng 11% app phát hành năm 2024 dùng Flutter và 7% dùng React Native.

**Native (Swift/SwiftUI cho iOS, Kotlin/Jetpack Compose cho Android)**
Hai codebase riêng, dùng công cụ chính thức của Apple và Google. Truy cập mọi API ngay khi hệ điều hành ra mắt, giao diện đúng chuẩn từng nền tảng. Đổi lại chi phí gần gấp đôi vì phải viết và bảo trì hai lần.

**Flutter (Google, ngôn ngữ Dart)**
Tự vẽ toàn bộ giao diện bằng engine riêng, nên UI giống hệt nhau trên mọi nền tảng. Chạy được trên iOS, Android, web, Windows, macOS, Linux. Engine [Impeller](https://docs.flutter.dev/perf/impeller) hiện là mặc định: là engine duy nhất trên iOS, và mặc định trên Android API 29 trở lên. Điều này giải quyết hiện tượng giật khi biên dịch shader mà Flutter từng bị chê.

**React Native (Meta, JavaScript/TypeScript)**
Viết bằng React, nhưng hiển thị bằng component native thật của hệ điều hành. Từ bản 0.76, [New Architecture](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture) (JSI, Fabric, TurboModules) là mặc định, thay cơ chế “bridge” cũ vốn là điểm nghẽn hiệu năng; từ bản 0.82 kiến trúc cũ bị bỏ hẳn. Dự án mới nên bắt đầu với **Expo**: lo sẵn build, cập nhật và các module native phổ biến.

**Kotlin Multiplatform (JetBrains, Kotlin)**
Chia sẻ logic nghiệp vụ (network, database, xử lý dữ liệu) giữa Android và iOS, còn UI có thể để native hoặc dùng chung bằng Compose Multiplatform. [Compose Multiplatform cho iOS](https://blog.jetbrains.com/kotlin/2025/05/compose-multiplatform-1-8-0-released-compose-multiplatform-for-ios-is-stable-and-production-ready/) đã stable từ bản 1.8.0 (05/2025). Hợp nhất với team Android muốn mở rộng sang iOS mà không viết lại từ đầu.

**.NET MAUI (Microsoft, C#)**
Phương án kế thừa Xamarin (Xamarin đã hết hỗ trợ từ 01/05/2024). Mỗi bản MAUI gắn với một bản .NET và có [chính sách hỗ trợ](https://dotnet.microsoft.com/en-us/platform/support/policy/maui) riêng, nên phải nâng cấp theo nhịp phát hành của .NET. Phù hợp khi công ty đã dùng .NET và Azure.

**Capacitor / Ionic (web trong WebView)**
Đóng gói web app (React, Vue, Angular…) thành app cài từ store, gọi tính năng native qua plugin. Nhanh nhất nếu đã có web, nhưng giao diện và hiệu năng kém mượt hơn các lựa chọn trên với app phức tạp.

**PWA (Progressive Web App)**
Web app cài lên màn hình chính, không qua store. Trên iOS, push notification chỉ hoạt động từ iOS 16.4 và chỉ khi người dùng đã “Thêm vào Màn hình chính” rồi mở app từ biểu tượng đó. Trên Android, PWA được hỗ trợ tốt hơn nhiều.

## 3. So sánh theo tiêu chí

| Công nghệ | Ngôn ngữ | Cách hiển thị UI | Hiệu năng | Truy cập tính năng native | Nền tảng | Chia sẻ code |
| --- | --- | --- | --- | --- | --- | --- |
| Native | Swift, Kotlin | Component của hệ điều hành | Cao nhất | Đầy đủ, có ngay khi OS ra mắt | iOS, Android riêng | Không chia sẻ |
| Flutter | Dart | Tự vẽ bằng engine Impeller | Gần native, animation mượt | Qua plugin hoặc platform channel | iOS, Android, web, desktop | Gần như toàn bộ, kể cả UI |
| React Native | TypeScript | Component native thật | Gần native với New Architecture | Qua module (Expo Modules, TurboModules) | iOS, Android; web qua React Native Web | Phần lớn, dùng chung được logic với web React |
| Kotlin Multiplatform | Kotlin | Native hoặc Compose Multiplatform | Gần native (biên dịch native) | Đầy đủ, gọi thẳng API mỗi nền tảng | iOS, Android, desktop; web đang beta | Tùy chọn: chỉ logic, hoặc cả UI |
| .NET MAUI | C# | Component native qua lớp trừu tượng | Khá | Qua .NET binding | iOS, Android, Windows, macOS | Phần lớn |
| Capacitor | TypeScript + web framework | HTML/CSS trong WebView | Thấp hơn với UI phức tạp | Qua plugin | iOS, Android, web | Gần như toàn bộ với web |
| PWA | TypeScript + web framework | Trình duyệt | Thấp nhất trong danh sách | Hạn chế, nhất là trên iOS | Mọi nền tảng có trình duyệt | Toàn bộ |

Cột “Hiệu năng” là đánh giá tương đối, không phải benchmark. Với đa số app nghiệp vụ (form, danh sách, gọi API), cả Flutter, React Native và KMP đều đủ nhanh. Khác biệt chỉ rõ ở animation phức tạp, xử lý ảnh, video hoặc thiết bị cấu hình yếu.

## 4. Yếu tố quyết định

Xếp theo mức độ ảnh hưởng, từ lớn đến nhỏ:

1. **Kỹ năng hiện có của team.** Đây là yếu tố nặng nhất. Team giỏi Dart chọn Flutter, team giỏi React chọn React Native, team Android chọn KMP, team .NET chọn MAUI. Đổi công nghệ vì “nghe nói nhanh hơn” thường tốn hơn phần lợi thu được.
2. **Mức độ phụ thuộc vào tính năng hệ điều hành.** App cần widget, Apple Watch, CarPlay, Bluetooth phức tạp, AR hay xử lý media thời gian thực thì native hoặc KMP sẽ ít vướng hơn.
3. **Giao diện:** muốn UI thương hiệu riêng, giống nhau trên mọi máy thì Flutter mạnh. Muốn UI đúng chuẩn từng nền tảng thì React Native, native hoặc KMP với UI native.
4. **Nền tảng cần hỗ trợ:** chỉ mobile, hay cả web và desktop? Flutter và Compose Multiplatform che được nhiều nền tảng nhất từ một codebase.
5. **Code đã có sẵn:** đã có web React thì React Native hoặc Capacitor; đã có app Android thì KMP.
6. **Ngân sách và thời gian:** một codebase đa nền tảng thường rẻ hơn hai team native, đặc biệt với MVP.
7. **Tuyển dụng và bàn giao:** nếu sau này giao cho khách hàng hoặc team khác, chọn công nghệ họ dễ tuyển người. Nên kiểm tra số tin tuyển dụng thực tế ở thành phố của bạn trước khi quyết.

**Câu hỏi cần trả lời trước khi chọn**

- [ ] Team (hoặc bạn) đã làm thật với ngôn ngữ nào?
- [ ] App cần những tính năng hệ điều hành nào? Đã có plugin/module ổn định cho từng tính năng chưa?
- [ ] Cần hỗ trợ nền tảng nào: iOS, Android, web, desktop?
- [ ] UI theo thương hiệu riêng hay theo chuẩn từng nền tảng?
- [ ] Ai sẽ bảo trì app sau 2 năm?

## 5. Khi code cùng AI (Claude Code, Copilot…)

Mục này là nhận định từ kinh nghiệm dùng AI, không phải số liệu đo đạc. AI viết code tốt nhất với công nghệ có nhiều code mẫu công khai, có kiểu dữ liệu chặt, và có cách kiểm tra nhanh (compiler, test, hot reload).

| Công nghệ | Thuận lợi khi dùng AI | Cần chú ý |
| --- | --- | --- |
| Flutter | Dart có kiểu chặt, một codebase cho mọi nền tảng, nhiều code mẫu, hot reload kiểm tra UI nhanh | Chỉ rõ phiên bản Flutter và thư viện state management (BLoC, Riverpod…) để AI không trộn nhiều kiểu |
| React Native | TypeScript và React là hệ sinh thái rất lớn, AI hiểu rất tốt | Nhiều code mẫu cũ dùng kiến trúc trước 0.76: dặn AI dùng Expo và New Architecture |
| Native (SwiftUI, Compose) | Tài liệu chính thức tốt, kiểu chặt | Phải viết hai lần; API thay đổi theo từng phiên bản hệ điều hành, nên ghi rõ iOS và Android tối thiểu |
| Kotlin Multiplatform | Kotlin kiểu chặt, AI hiểu Kotlin Android tốt | Compose Multiplatform cho iOS còn mới, ít code mẫu hơn, AI dễ đoán sai API |
| .NET MAUI | C# kiểu chặt | Cộng đồng nhỏ hơn, ít code mẫu mobile |

**Cách làm chung cho mọi công nghệ:**

- Ghi stack, phiên bản và cấu trúc thư mục vào `CLAUDE.md` (mẫu: [templates/CLAUDE.md](../templates/CLAUDE.md)), hoặc `AGENTS.md` nếu team dùng nhiều công cụ AI.
- Tạo trước một feature mẫu thật chuẩn để AI bắt chước.
- Bật lint và analyzer ở mức chặt, để AI tự sửa lỗi theo thông báo của công cụ.
- Luôn test trên máy thật, đặc biệt máy Android cấu hình thấp.

## 6. Build, phát hành và cập nhật

Chọn công nghệ xong, đừng quên phần chi phí và quy trình ra store. Phần này ảnh hưởng đến lựa chọn nhiều hơn người ta nghĩ.

**Build và tài khoản**

- **Build iOS cần macOS và Xcode.** Không có Mac thì dùng dịch vụ build cloud: [EAS Build](https://docs.expo.dev/build/introduction/) (Expo), [Codemagic](https://codemagic.io) (Flutter, React Native, native), hoặc GitHub Actions với runner macOS. Đều có gói miễn phí giới hạn số phút.
- **Phí tài khoản:** Apple Developer Program $99/năm, Google Play $25 một lần. Đăng ký tên tổ chức (không phải cá nhân) cần mã số D-U-N-S, nên làm sớm vì có thể mất vài tuần.
- **Ký app:** giữ keystore Android và chứng chỉ iOS ở nơi an toàn có backup; mất keystore là không cập nhật được app cũ trên Google Play (trừ khi dùng Play App Signing).

**Cập nhật không qua store (OTA)**

| Công nghệ | Công cụ | Cập nhật được gì |
| --- | --- | --- |
| React Native (Expo) | [EAS Update](https://docs.expo.dev/eas-update/introduction/) | Code JavaScript và asset; thay đổi native vẫn phải lên store |
| Flutter | [Shorebird](https://shorebird.dev) | Code Dart; thay đổi native và plugin mới vẫn phải lên store |
| Native, KMP | Không có cơ chế tương đương phổ biến | Mọi thay đổi qua store; dùng feature flag / remote config để bật tắt tính năng |

OTA hợp để sửa lỗi gấp. Không dùng OTA để thêm tính năng lớn hay đổi mục đích app nhằm né review: Apple cấm tải code làm đổi chức năng app (guideline 2.5.2) và tính năng ẩn (2.5.19), Google cũng có quy định tương tự; app có thể bị gỡ. Danh sách rủi ro store đầy đủ: [Dùng Claude để test web app và mobile app, mục 11.2](claude-test-web-mobile.md#112-rủi-ro-bị-app-store--google-play-từ-chối).

**Sau khi phát hành:** cài crash report (Crashlytics, Sentry) và analytics ngay từ bản đầu, kèm một remote config / feature flag để tắt nhanh tính năng lỗi mà không cần chờ review.

## 7. Gợi ý theo loại app và prompt mẫu

| Loại app | Gợi ý | Lý do |
| --- | --- | --- |
| App nghiệp vụ, quản lý, POS, cần offline | Flutter hoặc React Native | UI form và danh sách, có thư viện database local tốt, một team làm cả hai nền tảng |
| App thương mại điện tử, nội dung | React Native hoặc Flutter | Nếu đã có web React thì React Native chia sẻ được nhiều hơn |
| App có UI thương hiệu nặng, nhiều animation | Flutter | Tự vẽ UI, giống nhau trên mọi máy |
| App ngân hàng, sức khỏe | Native hoặc KMP nếu cần tích hợp OS sâu; Flutter hoặc React Native vẫn dùng được (nhiều ngân hàng đang dùng) | Bảo mật phụ thuộc cách làm (lưu trữ an toàn, certificate pinning, kiểm tra thiết bị) nhiều hơn framework; native dễ dùng API bảo mật mới nhất |
| App chỉ hiển thị nội dung web có sẵn | Capacitor hoặc PWA | Tận dụng web, ít công sức |
| Game | Unity, Godot hoặc engine game | Các framework app phía trên không dành cho game |

**Prompt mẫu: chọn công nghệ cho dự án**

```text
Bạn là mobile architect. Dự án của tôi: <mô tả app, người dùng, số lượng dự kiến>.
Tính năng cần hệ điều hành: <camera, Bluetooth, push, offline, widget, thanh toán…>.
Team: <số người, ngôn ngữ đã thành thạo>. Nền tảng cần: <iOS, Android, web, desktop>.
So sánh Flutter, React Native (Expo), Kotlin Multiplatform và Native cho dự án này.
Với mỗi tính năng hệ điều hành, cho biết plugin/module phổ biến và mức độ ổn định, kèm link.
Kết luận một lựa chọn và 3 rủi ro lớn nhất của lựa chọn đó.
```

**Prompt mẫu: kiểm tra một tính năng khó trước khi cam kết**

```text
Tôi định làm app bằng <Flutter>. App cần <kết nối máy in nhiệt qua Bluetooth / widget màn hình chính / chạy nền định vị>.
Tìm các thư viện đang được duy trì cho tính năng này, ngày release gần nhất, issue mở lớn nhất.
Nếu phải tự viết code native, ước lượng công sức cho iOS và Android. Ghi nguồn cho mọi thông tin.
```

**Prompt mẫu: khởi tạo dự án với Claude Code**

```text
Tạo dự án <Flutter / React Native Expo> cho app <tên>, phiên bản mới nhất ổn định.
Cấu trúc feature-first, state management <BLoC / Zustand>, database local <drift / SQLite>, i18n tiếng Việt và tiếng Anh.
Tạo sẵn một feature mẫu hoàn chỉnh (màn hình, state, repository, test) và viết CLAUDE.md theo mẫu templates/CLAUDE.md:
cấu trúc, lệnh build và test, quy ước, điều cấm.
```

## Nguồn

- [Cross-platform mobile development – The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/cross-platform-mobile-development)
- [Impeller rendering engine – Flutter docs](https://docs.flutter.dev/perf/impeller)
- [React Native 0.76: New Architecture by default – React Native blog](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture)
- [Compose Multiplatform 1.8.0: iOS stable – JetBrains](https://blog.jetbrains.com/kotlin/2025/05/compose-multiplatform-1-8-0-released-compose-multiplatform-for-ios-is-stable-and-production-ready/)
- [Kotlin Multiplatform roadmap 2025 – JetBrains](https://blog.jetbrains.com/kotlin/2024/10/kotlin-multiplatform-development-roadmap-for-2025/)
- [.NET MAUI Support Policy – Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/maui)
- [PWA iOS limitations – MagicBell](https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide)
- [Stack Overflow Developer Survey 2025 – Technology](https://survey.stackoverflow.co/2025/technology/)
- [EAS Build](https://docs.expo.dev/build/introduction/) · [EAS Update](https://docs.expo.dev/eas-update/introduction/) · [Shorebird](https://shorebird.dev) · [Codemagic](https://codemagic.io)
- [Apple Developer Program](https://developer.apple.com/programs/) · [Google Play — Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756)
