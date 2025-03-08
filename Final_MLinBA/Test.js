import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import StatisticsTabSection from './statistics-tab-section';

describe('StatisticsTabSection', () => {
  test('renders menubar', () => {
    render(<StatisticsTabSection />);
    const menubar = screen.getByRole('banner');
    expect(menubar).toBeInTheDocument();
  });

  test('renders tab container with two tabs', () => {
    render(<StatisticsTabSection />);
    const tabContainer = screen.getByRole('tablist');
    expect(tabContainer).toBeInTheDocument();
    const tabs = screen.getAllByRole('tab');
    expect(tabs).toHaveLength(2);
  });

  test('renders sidebar with menu items', () => {
    render(<StatisticsTabSection />);
    const sidebar = screen.getByRole('navigation');
    expect(sidebar).toBeInTheDocument();
    const menuItems = screen.getAllByRole('menuitem');
    expect(menuItems.length).toBeGreaterThan(0);

    // Kiểm tra danh sách menu items mong đợi
    const expectedItems = ['Overview', 'Trends', 'Reports']; // Thay bằng menu thực tế của bạn
    expectedItems.forEach((item) => {
      expect(screen.getByText(item)).toBeInTheDocument();
    });
  });

  test('renders main content with sections', () => {
    render(<StatisticsTabSection />);
    const mainContent = screen.getByRole('main');
    expect(mainContent).toBeInTheDocument();
    const sections = screen.getAllByRole('heading', { level: 2 });
    expect(sections).toHaveLength(2);
  });

  test('dropdown menu is accessible and toggles on click', () => {
    render(<StatisticsTabSection />);
    const dropdownToggle = screen.getByRole('button', { name: /response rate/i });

    expect(dropdownToggle).toHaveAttribute('aria-expanded', 'false');

    // Kích hoạt dropdown
    fireEvent.click(dropdownToggle);
    expect(dropdownToggle).toHaveAttribute('aria-expanded', 'true');

    // Đóng dropdown
    fireEvent.click(dropdownToggle);
    expect(dropdownToggle).toHaveAttribute('aria-expanded', 'false');
  });

  test('switches tab content when clicking tabs', () => {
    render(<StatisticsTabSection />);
    const tabStatistics = screen.getByRole('tab', { name: /Statistics/i });
    const tabML = screen.getByRole('tab', { name: /Machine Learning/i });

    // Ban đầu hiển thị Statistics
    expect(screen.getByText(/Statistics Content/i)).toBeInTheDocument();

    // Chuyển sang tab Machine Learning
    fireEvent.click(tabML);
    expect(screen.getByText(/Machine Learning Content/i)).toBeInTheDocument();

    // Quay lại tab Statistics
    fireEvent.click(tabStatistics);
    expect(screen.getByText(/Statistics Content/i)).toBeInTheDocument();
  });
});
